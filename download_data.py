import wget
import os
import zipfile


download_folder = "Webis-data"
os.makedirs(download_folder, exist_ok=True)

file_url = "https://zenodo.org/api/records/5776081/files-archive"
file_path = os.path.join(download_folder, 'data.zip')


# Download step
if not os.path.exists(file_path):
    print("Downloading main file...")
    wget.download(file_url, out=file_path)
    print(f"\nFile downloaded to {file_path}")
else:
    print("Main ZIP file already exists, skipping download.")

# Extract all ZIPs directly into the main 'extracted' folder
extract_folder = os.path.join(download_folder, 'extracted')
os.makedirs(extract_folder, exist_ok=True)

def extract_zip(zip_path, target_folder):
    """Extracts a ZIP file and returns any nested ZIPs found"""
    nested_zips = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)
        # Check for nested ZIPs in the extracted files
        for extracted_file in zip_ref.namelist():
            if extracted_file.endswith('.zip'):
                nested_zips.append(os.path.join(target_folder, extracted_file))
    return nested_zips

# Process main ZIP and all nested ones
if not os.listdir(extract_folder):  # Only extract if folder is empty
    print("Extracting files...")
    zip_queue = [file_path]
    
    while zip_queue:
        current_zip = zip_queue.pop(0)
        if os.path.exists(current_zip):
            new_zips = extract_zip(current_zip, extract_folder)
            zip_queue.extend(new_zips)
            # Remove the ZIP after extraction (optional)
            os.remove(current_zip)
    
    print(f"All files extracted to: {extract_folder}")
else:
    print("Extracted files already exist, skipping extraction.")


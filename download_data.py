import wget
import os

download_folder = "Webis-data"
os.makedirs(download_folder, exist_ok=True)

file_url = "https://zenodo.org/api/records/5776081/files-archive"
file_path = os.path.join(download_folder, 'data.zip')

wget.download(file_url, out=file_path)
print(f"\nFile downloaded to {file_path}")
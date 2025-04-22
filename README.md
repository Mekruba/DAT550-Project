# Hyperpartisan News Detection with CNN and Decision tree
This project is part of the DAT550 - Machine Learning course and focuses on detecting hyperpartisan news articles. The advanced solution has Convolutional Neural Network (CNN) implemented with TensorFlow/Keras and the simple has Traditional machine learning methods such as regression and decision trees.

## Requirements
- Python 3.12
Install the necessary dependencies using:
```bash
pip install -r requirements.txt
```

## Data Setup
You can download and preprocess the dataset using the following scripts:
### 1. Download Raw Data
Downloading the raw data may take a few minutes.

Run:
```bash
python downloaded_data.py
```
### 2. Preprocess Data
Change into preprocessing directory and the run the python script to
convert the XML files into structured JSONL format:
```bash
cd ./preprocessing
python preprocess.py
```
### 3. Expected Directory Structure
Ensure that the following data files exist in the specified locations:
```bash
preprocessing/data/
├── articles-test-byarticle.jsonl               # Test articles
├── articles-training-byarticle.jsonl           # Training articles
├── ground-truth-training-byarticle.jsonl       # Training labels
└── ground-truth-test-byarticle.jsonl           # Test labels

```
## Getting Started

After setting up the data, you can train and views the models in:

- Project-TraditinalML.ipynb
- Project.ipynb
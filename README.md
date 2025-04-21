# Hyperpartisan News Detection with CNN and Decision tree
This project is part of the DAT550 - Machine Learning course and focuses on detecting hyperpartisan news articles. The solution combines a Convolutional Neural Network (CNN) implemented with TensorFlow/Keras and a Decision Tree classifier from traditional machine learning methods.

## Requirements
- Python 3.12
Install the necessary dependencies using:
```bash
pip install -r requirements.txt
```

## Data Setup
You can download and preprocess the dataset using the following scripts:
### 1. Download Raw Data
Run:
```bash
python downloaded_data.py
```
### 2. Preprocess Data
Convert the XML files into structured JSONL format:
```bash
python preprocess.py
```
### 3. Expected Directory Structure
Ensure that the following data files exist in the specified locations:
```bash
preprocessing/data/
├── articles-training-byarticle.jsonl           # Training articles
├── ground-truth-training-byarticle.jsonl       # Training labels
├── articles-test-byarticle.jsonl               # Test articles
└── ground-truth-test-byarticle.jsonl           # Test labels

```
## Getting Started
After setting up the data, you can train the models by running:
```bash
python train_cnn.py      # For CNN model
python train_tree.py     # For Decision Tree model

```

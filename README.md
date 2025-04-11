# Hyperpartisan News Detection with CNN and Decision tree

This project is part of the DAT550 course and aims to detect hyperpartisan news articles using a Convolutional Neural Network (CNN) built with TensorFlow/Keras and Decision tree.



## Requirements

The code runs on Python 3.12

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Training and test data 
The training and test data can be fetched with `downloaded_data.py` file, then preprocessed with `preprocess.py` to process the xml files into json files. The data files should have the path as shown below.
- `preprocessing/data/articles-training-byarticle.jsonl` – Training articles  
- `preprocessing/data/ground-truth-training-byarticle.jsonl` – Training labels  
- `preprocessing/data/articles-test-byarticle.jsonl` – Test articles  
- `preprocessing/data/ground-truth-test-byarticle.jsonl` – Test labels  

# Hyper-Partisan News Detection: Traditional ML Workflow

## Step 1: Feature Extraction
Choose features that capture linguistic and stylistic bias:

### Lexical Features
- **Bag-of-Words (BoW)**: Unigrams/bigrams (e.g., "radical left," "far-right")
- **TF-IDF**: Weight words by importance (downweights frequent but meaningless words like "the")

### Stylometric Features
- **Punctuation counts**: Exclamation marks, question marks, ALL-CAPS words
- **Readability scores** (e.g., Flesch-Kincaid)
- **Sentence/word length**: Hyper-partisan text may be shorter/more aggressive

### Sentiment/Emotion Features
- **Polarity/subjectivity** (e.g., using VADER lexicon)
- **Emotion words** (anger, fear) from lexicons like LIWC

### Structural Features
- **Quotation-to-text ratio**: High ratio may indicate neutrality
- **Named entities**: Overuse of partisan groups (e.g., "Antifa," "MAGA")

### Metadata (if available)
- **Source/outlet bias** (pre-labeled, e.g., Breitbart vs. Reuters)
- **Publication date** (election periods may increase bias)

## Step 2: Preprocessing
1. **Clean text**: Remove URLs, punctuation, lowercase all words
2. **Tokenization**: Split text into words/sentences
3. **Stopword removal**: Exclude common words (e.g., "the," "and")
4. **Lemmatization**: Reduce words to base forms (e.g., "running" → "run")

## Step 3: Train-Test Split
- Split data into **70% training, 30% testing** (or 80/20)
- **Stratified sampling**: Ensure balanced class distribution (hyper-partisan vs. neutral)

## Step 4: Model Selection
Pick interpretable models for feature analysis:

1. **Logistic Regression**
   - Works well with TF-IDF
   - Provides coefficients to identify biased words (e.g., "corrupt" → high weight)

2. **Random Forest**
   - Handles non-linear relationships
   - Feature importance shows which words/styles matter most

3. **SVM (Linear Kernel)**
   - Effective for high-dimensional text data
   - Robust to overfitting with regularization

4. **XGBoost**
   - Gradient-boosted trees for higher accuracy
   - Requires more hyperparameter tuning

## Step 5: Model Training
1. **Vectorize text**: Convert features (e.g., TF-IDF for BoW)
2. **Scale features**: Normalize stylometric/sentiment scores (e.g., using `StandardScaler`)
3. **Train classifier**: Fit model on training data

## Step 6: Evaluation
Use metrics suited for imbalanced data:
- **Precision/Recall/F1-score** (better than accuracy)
  - Precision: % of detected hyper-partisan articles that are correct
  - Recall: % of actual hyper-partisan articles detected
- **Confusion Matrix**: Visualize false positives/negatives
- **ROC-AUC**: Measures model's ranking capability

## Step 7: Interpretability
1. **Logistic Regression**: Check coefficients for most biased words
2. **Random Forest**: Plot feature importances (e.g., exclamation marks matter?)
3. **Error Analysis**: Manually review misclassified articles to refine features

## Step 8: Improvements (Optional)
1. **Feature Selection**
   - Use `SelectKBest` or PCA to reduce noise
2. **Class Weighting**
   - Adjust for class imbalance (e.g., `class_weight='balanced'` in sklearn)
3. **Ensemble Methods**
   - Combine models (e.g., SVM + Random Forest) via voting

## Tools to Use (No Code Needed)
- **Data Annotation**: Label hyper-partisan vs. neutral (if not already labeled)
- **Feature Extraction**: `sklearn`'s `TfidfVectorizer`, `CountVectorizer`
- **Models**: `sklearn`'s `LogisticRegression`, `RandomForestClassifier`, `SVM`
- **Evaluation**: `sklearn`'s `classification_report`, `confusion_matrix`

## Key Takeaways
- **Best features**: TF-IDF + stylometry + sentiment
- **Best models**: Logistic Regression (interpretable) or Random Forest (robust)
- **Tune hyperparameters**: Grid search for optimal settings
# Fake-Review-Detection
Fake  Review Detection using NLP

## Dataset
This project uses the Yelp Academic Dataset.

Due to GitHub file size limits, the dataset is not included in this repository.

Download link:
https://www.yelp.com/dataset

After downloading, place the files inside:
data/


# 🕵️‍♂️ Fake Review Detection System

## 📌 Overview

Online review platforms often suffer from **fake or manipulative reviews** that mislead users and harm trust. This project builds an **end-to-end Machine Learning pipeline** to detect fake reviews using **textual patterns and behavioral features**, with a strong focus on **model validation and interpretability**.

The system is designed following **industry-style ML practices**:

* Clear separation of preprocessing, feature extraction, modeling, and evaluation
* Handling of class imbalance
* Feature ablation for robustness checks
* Model interpretability using Logistic Regression coefficients

---

## 🎯 Objectives

* Detect **fake vs genuine reviews** (binary classification)
* Learn meaningful linguistic patterns instead of heuristic shortcuts
* Validate robustness using feature ablation
* Provide explainable insights into model predictions

---

## 🗂️ Project Structure

```
│fake-review-detection/
│── data/
│ ├── reviews_clean.csv # cleaned raw reviews
│ ├── reviews_labeled.csv # reviews with fake/genuine labels
│ ├── reviews_preprocessed.csv # text-cleaned reviews used for TF-IDF
│ ├── reviews_with_features.csv # reviews + engineered numeric features
│ ├── X_features.npz # TF-IDF + numeric features (with stars)
│ ├── X_features_no_stars.npz # TF-IDF + numeric features (without stars)
│ ├── sample_reviews.json
│── models/
│ ├── logistic_regression_no_stars.pkl
│ └── tfidf_vectorizer.pkl
│
│── notebooks/
│ ├── preprocessing.ipynb
│ ├── feature_extraction.ipynb
│ ├── model.ipynb
│ └── analysis.ipynb
│
│── README.md
```

---

## 🧪 Dataset

* Review text data (preprocessed)
* Each review labeled as:

  * `0` → Genuine
  * `1` → Fake

⚠️ **Note:** Labels were generated using heuristic rules to simulate fake review behavior. This is acknowledged and validated through feature ablation.

---

## ⚙️ Preprocessing

Performed in `preprocessing.ipynb`:

* Lowercasing
* Removing punctuation & numbers
* Stopword removal
* Lemmatization
* Cleaned text stored as `text_clean`

---

## 🧩 Feature Engineering

Performed in `feature_extraction.ipynb`.

### 1️⃣ Text Features (TF-IDF)

* **TfidfVectorizer**
* Unigrams + Bigrams
* Parameters:

  * `max_features=5000`
  * `ngram_range=(1,2)`
  * `min_df=5`, `max_df=0.8`

### 2️⃣ Behavioral Features

* `review_length`
* `char_length`
* `exclamation_count`
* `question_count`
* (`stars` feature initially included, later removed)

### 3️⃣ Feature Matrix

* Combined using `scipy.sparse.hstack`
* Saved as `.npz` for efficient reuse

---

## 🤖 Model Training

Performed in `model.ipynb`.

### Model Used

* **Logistic Regression**

### Why Logistic Regression?

* Strong baseline for text classification
* Works well with sparse TF-IDF features
* Highly interpretable via coefficients

### Training Details

* `class_weight='balanced'` (to handle class imbalance)
* `max_iter=1000`
* 80/20 Train-Test Split with `stratify=y`

---

## 📊 Evaluation Results

### 🔹 With all features

* **Accuracy:** ~96.1%
* **Fake review recall:** 96%
* **Fake review F1-score:** 0.92

### 🔹 Feature Ablation (Stars Removed)

* **Accuracy:** 96.13%
* **Fake review recall:** 96%
* **No performance drop observed**

✅ Confirms the model does **not rely on star ratings** and learns from textual patterns.

---

## 🧠 Model Interpretability (Key Highlight)

Using Logistic Regression coefficients, we analyzed the most influential features.

### 🔴 Top indicators of **Fake Reviews**

* Overly promotional phrases:

  * `highly recommend`
  * `best ever`
  * `must`
* Repetitive recommendation language
* Excessive punctuation (`exclamation_count`, `question_count`)

### 🟢 Top indicators of **Genuine Reviews**

* Contextual and experiential words:

  * `lunch`, `tea`, `vegan`, `great atmosphere`
* Balanced recommendation phrases:

  * `would recommend`, `definitely recommend`
* Natural conversational fillers (`oh`, `yes`)

📌 This confirms the model captures **real linguistic differences** between fake and genuine reviews.

---

## ✅ Key Takeaways

* Built a **robust fake review detector** with 96% accuracy
* Validated model behavior using **feature ablation**
* Ensured **no data leakage** from star ratings
* Achieved **interpretability**, not just high accuracy
* Followed **production-style ML pipeline design**

---

## 🚀 Future Improvements

* Try Linear SVM / XGBoost for comparison
* Add ROC–AUC and Precision–Recall curves
* Deploy as a Flask API for real-time prediction
* Test on a fully human-labeled dataset

---

## 🧑‍💻 Author

**Dev**
B.Tech Electrical Engineering, DTU
Interests: Machine Learning, Backend Development, Applied NLP

---

⭐ If you found this project insightful, feel free to star the repository!



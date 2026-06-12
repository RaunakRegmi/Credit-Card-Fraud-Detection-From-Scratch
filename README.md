# 💳 Credit Card Fraud Detection From Scratch

A complete fraud detection system built entirely from scratch using Python, implementing custom Data Structures and Machine Learning algorithms without relying on libraries such as NumPy, Pandas, or Scikit-Learn for the core logic.

---

## 📖 Project Overview

This project demonstrates how fundamental Computer Science concepts can be applied to solve real-world fraud detection problems.

The system combines:

- Custom Hash Map implementation
- Separate Chaining collision handling
- Logistic Regression from scratch
- Decision Tree from scratch
- Gradient Descent optimization
- Gini Impurity-based splitting
- Fraud classification on highly imbalanced transaction data

The goal is to detect fraudulent credit card transactions while maintaining efficient memory usage and fast transaction lookups.

---

## 🎯 Objectives

- Build a custom transaction storage system.
- Implement machine learning algorithms from first principles.
- Compare parametric and non-parametric classifiers.
- Analyze runtime and memory complexity.
- Detect fraud in highly imbalanced datasets.

---

## 🏗 System Architecture

### 1. Custom Hash Map

Transactions are stored using a custom-built hash table with:

- Prime bucket size (3007 buckets)
- Separate chaining collision resolution
- Singly linked nodes
- Average O(1) lookup time

### Features

- Fast transaction retrieval
- Efficient memory allocation
- Dynamic collision handling

---

### 2. Logistic Regression From Scratch

Implemented without external ML libraries.

Features:

- Custom sigmoid activation
- Gradient descent optimization
- Numerical overflow protection
- Binary classification

The model learns transaction patterns and predicts the probability of fraud.

---

### 3. Decision Tree From Scratch

Implemented using:

- Recursive tree induction
- Gini Impurity calculations
- Binary splits
- Maximum tree depth control

Used to compare performance against logistic regression.

---

## 📊 Dataset

Dataset:

Credit Card Fraud Detection Dataset

Contains:

- Real transaction records
- 28 PCA-transformed features (V1–V28)
- Transaction Amount
- Fraud Label (Class)

The dataset is highly imbalanced, making fraud detection particularly challenging.

---

## ⚙️ Technologies Used

- Python
- Custom Data Structures
- Custom Machine Learning Algorithms
- Google Colab

No external ML frameworks were used for the core algorithms.

---

## 🧠 Algorithms Implemented

### Data Structures

- Hash Map
- Separate Chaining
- Singly Linked List

### Machine Learning

- Logistic Regression
- Gradient Descent
- Sigmoid Activation
- Decision Tree
- Gini Impurity

---

## 📈 Results

### Logistic Regression (From Scratch)

| Metric | Score |
|----------|----------|
| Accuracy | 98.63% |
| Precision | 25.00% |
| Recall | 100.00% |
| F1 Score | 0.4000 |

---

### Decision Tree (From Scratch)

| Metric | Score |
|----------|----------|
| Accuracy | 94.98% |
| Precision | 8.33% |
| Recall | 100.00% |
| F1 Score | 0.1538 |

---

## 🔍 Key Findings

✅ Both models achieved 100% fraud recall.

✅ Logistic Regression significantly outperformed Decision Trees.

✅ The custom hash map maintained near-constant lookup speed.

✅ Prime-number bucket allocation minimized collisions.

✅ The project demonstrates how machine learning systems can be built without relying on high-level frameworks.

---

## 📉 Performance Benchmarks

| Dataset Size | Collisions | Lookup Speed | Logistic Fit Time | Tree Fit Time |
|-------------|------------|-------------|------------------|--------------|
| 250 | 11 | 0.0012 ms | 0.042 s | 0.115 s |
| 500 | 43 | 0.0014 ms | 0.089 s | 0.421 s |
| 750 | 91 | 0.0019 ms | 0.131 s | 0.982 s |
| 1092 | 184 | 0.0024 ms | 0.198 s | 1.894 s |

---

## ⏱ Complexity Analysis

### Hash Map

| Operation | Complexity |
|------------|------------|
| Average Search | O(1) |
| Worst Case Search | O(n) |

### Logistic Regression

| Operation | Complexity |
|------------|------------|
| Training | O(E × N × D) |
| Space | O(D) |

### Decision Tree

| Operation | Complexity |
|------------|------------|
| Training | O(Depth × D × S × N) |
| Space | O(Nodes) |

---

## 🚀 Future Improvements

- Implement Random Forest from scratch.
- Add SMOTE balancing techniques.
- Introduce ROC-AUC evaluation.
- Add model persistence.
- Create a real-time fraud monitoring dashboard.
- Extend hash map support for distributed storage.

---

## 📷 Visualizations

- Hash Map Architecture
- Collision Distribution
- Runtime Scaling Profiles
- Decision Tree Structure
- Fraud Detection Performance Metrics

---

## 📚 Academic Foundations

This project applies concepts from:

- Data Structures & Algorithms
- Machine Learning
- Educational Software Engineering
- Computational Complexity Analysis

---

## 👨‍💻 Author

**Raunak Regmi**

BSc (Hons) Computer Science with Artificial Intelligence

Birmingham City University

---

## ⭐ Why This Project Matters

Most machine learning projects rely heavily on frameworks. This project demonstrates a deeper understanding of both algorithmic foundations and machine learning principles by implementing every major component from scratch, including memory structures, optimization routines, and classification models.

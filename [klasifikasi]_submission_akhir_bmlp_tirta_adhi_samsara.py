# -*- coding: utf-8 -*-
"""[Klasifikasi] Submission Akhir BMLP_TIRTA ADHI SAMSARA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J53cuP-LmUVOG3gzwqzmhKIf01uw83-t

# **1. Import Library**

Pada tahap ini, Anda perlu mengimpor beberapa pustaka (library) Python yang dibutuhkan untuk analisis data dan pembangunan model machine learning.
"""

# Import Library
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

"""# **2. Memuat Dataset dari Hasil Clustering**

Memuat dataset hasil clustering dari file CSV ke dalam variabel DataFrame.
"""

# Memuat Dataset Hasil Clustering
dataset = pd.read_csv('/content/Hasil_Clustering_Cuy.csv')
print("Dataset Loaded Successfully.")
print(dataset.head())

# Memisahkan fitur dan target
X = dataset.drop(columns=['cluster'])  # Semua kolom kecuali Cluster
y = dataset['cluster']                # Kolom Cluster sebagai target

"""# **3. Data Splitting**

Tahap Data Splitting bertujuan untuk memisahkan dataset menjadi dua bagian: data latih (training set) dan data uji (test set).
"""

# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("Data Splitting Done.")
print(f"Data Latih: {X_train.shape[0]} baris, Data Uji: {X_test.shape[0]} baris")

"""# **4. Membangun Model Klasifikasi**

## **a. Membangun Model Klasifikasi**

Setelah memilih algoritma klasifikasi yang sesuai, langkah selanjutnya adalah melatih model menggunakan data latih.

Berikut adalah rekomendasi tahapannya.
1. Pilih algoritma klasifikasi yang sesuai, seperti Logistic Regression, Decision Tree, Random Forest, atau K-Nearest Neighbors (KNN).
2. Latih model menggunakan data latih.
"""

# Model 1: Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Model 2: Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

print("Model Training Selesai.")

"""Tulis narasi atau penjelasan algoritma yang Anda gunakan.

## **b. Evaluasi Model Klasifikasi**

Berikut adalah **rekomendasi** tahapannya.
1. Lakukan prediksi menggunakan data uji.
2. Hitung metrik evaluasi seperti Accuracy dan F1-Score (Opsional: Precision dan Recall).
3. Buat confusion matrix untuk melihat detail prediksi benar dan salah.
"""

# Prediksi Data Uji
rf_y_pred = rf_model.predict(X_test)
dt_y_pred = dt_model.predict(X_test)

# Evaluasi Random Forest
print("Random Forest Classifier:")
print(f"Accuracy: {accuracy_score(y_test, rf_y_pred):.2f}")
print(f"F1-Score: {f1_score(y_test, rf_y_pred, average='weighted'):.2f}")
print(f"Precision: {precision_score(y_test, rf_y_pred, average='weighted'):.2f}")
print(f"Recall: {recall_score(y_test, rf_y_pred, average='weighted'):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, rf_y_pred))

# Confusion Matrix untuk Random Forest
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, rf_y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix: Random Forest')
plt.show()

# Evaluasi Decision Tree
print("\nDecision Tree Classifier:")
print(f"Accuracy: {accuracy_score(y_test, dt_y_pred):.2f}")
print(f"F1-Score: {f1_score(y_test, dt_y_pred, average='weighted'):.2f}")
print(f"Precision: {precision_score(y_test, dt_y_pred, average='weighted'):.2f}")
print(f"Recall: {recall_score(y_test, dt_y_pred, average='weighted'):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, dt_y_pred))

# Confusion Matrix untuk Decision Tree
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, dt_y_pred), annot=True, fmt='d', cmap='Greens')
plt.title('Confusion Matrix: Decision Tree')
plt.show()

"""Tulis hasil evaluasi algoritma yang digunakan, jika Anda menggunakan 2 algoritma, maka bandingkan hasilnya.

saya menggunakan 2 model klasifikasi dengan hasil:
*  Random Forest: Accuracy, Precision, Recall, dan F1-Score: Semua metrik mencapai nilai 1.00.
*  Decision Tree: Accuracy, Precision, Recall, dan F1-Score: Semua metrik mencapai nilai 1.00.

## **c. Tuning Model Klasifikasi (Optional)**

Gunakan GridSearchCV, RandomizedSearchCV, atau metode lainnya untuk mencari kombinasi hyperparameter terbaik
"""



"""## **d. Evaluasi Model Klasifikasi setelah Tuning (Optional)**

Berikut adalah rekomendasi tahapannya.
1. Gunakan model dengan hyperparameter terbaik.
2. Hitung ulang metrik evaluasi untuk melihat apakah ada peningkatan performa.
"""



"""## **e. Analisis Hasil Evaluasi Model Klasifikasi**

Berikut adalah **rekomendasi** tahapannya.
1. Bandingkan hasil evaluasi sebelum dan setelah tuning (jika dilakukan).
2. Identifikasi kelemahan model, seperti:
  - Precision atau Recall rendah untuk kelas tertentu.
  - Apakah model mengalami overfitting atau underfitting?
3. Berikan rekomendasi tindakan lanjutan, seperti mengumpulkan data tambahan atau mencoba algoritma lain jika hasil belum memuaskan.

2. Identifikasi Kelemahan model:

Kedua model menunjukkan akurasi 100%, yang sangat jarang terjadi. Hal ini mengindikasikan bahwa kedua model kemungkinan besar mengalami overfitting, di mana model terlalu fokus pada detail data pelatihan sehingga kurang mampu melakukan generalisasi dengan baik pada data baru.

3. Rekomendasi tindakan lanjutan:

saya sudah puas dengan hasil yang didapat, namun untuk memastikannya agar lebih baik lagi dapat mencoba dengan algoritma lain selain yang saya pakai dan gunakan metode seperti k-fold cross-validation untuk mengukur performa model lebih akurat.
"""
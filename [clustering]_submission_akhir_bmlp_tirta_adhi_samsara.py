# -*- coding: utf-8 -*-
"""[Clustering] Submission Akhir BMLP_TIRTA ADHI SAMSARA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cam5Zs1CLadFgUnHnZzZMcD7_1UvM10w

# **1. Perkenalan Dataset**

Tahap pertama, Anda harus mencari dan menggunakan dataset **tanpa label** dengan ketentuan sebagai berikut:

1. **Sumber Dataset**:  
   Dataset dapat diperoleh dari berbagai sumber, seperti public repositories (*Kaggle*, *UCI ML Repository*, *Open Data*) atau data primer yang Anda kumpulkan sendiri.
   
2. **Ketentuan Dataset**:
   - **Tanpa label**: Dataset tidak boleh memiliki label atau kelas.
   - **Jumlah Baris**: Minimal 1000 baris untuk memastikan dataset cukup besar untuk analisis yang bermakna.
   - **Tipe Data**: Harus mengandung data **kategorikal** dan **numerikal**.
     - *Kategorikal*: Misalnya jenis kelamin, kategori produk.
     - *Numerikal*: Misalnya usia, pendapatan, harga.

3. **Pembatasan**:  
   Dataset yang sudah digunakan dalam latihan clustering (seperti customer segmentation) tidak boleh digunakan.
"""

#Dataset menggunakan Customer Personality Analysis sesuai yang disarankan, di download pada websie kaggle https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

"""# **2. Import Library**

Pada tahap ini, Anda perlu mengimpor beberapa pustaka (library) Python yang dibutuhkan untuk analisis data dan pembangunan model machine learning.
"""

# Import library yang diperlukan
import pandas as pd  # Untuk manipulasi dan analisis data
import numpy as np  # Untuk operasi numerik
import matplotlib.pyplot as plt  # Untuk visualisasi data
import seaborn as sns  # Untuk visualisasi data yang lebih menarik

# Menggunakan algoritma KMeans untuk clustering
from sklearn.cluster import KMeans

# Menggunakan metrik evaluasi clustering, seperti silhouette score
from sklearn.metrics import silhouette_score

# Menggunakan preprocessing untuk standarisasi data numerik dan encoding data kategorikal
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Menggunakan PCA (Principal Component Analysis) untuk reduksi dimensi
from sklearn.decomposition import PCA

"""# **3. Memuat Dataset**

Pada tahap ini, Anda perlu memuat dataset ke dalam notebook. Jika dataset dalam format CSV, Anda bisa menggunakan pustaka pandas untuk membacanya. Pastikan untuk mengecek beberapa baris awal dataset untuk memahami strukturnya dan memastikan data telah dimuat dengan benar.

Jika dataset berada di Google Drive, pastikan Anda menghubungkan Google Drive ke Colab terlebih dahulu. Setelah dataset berhasil dimuat, langkah berikutnya adalah memeriksa kesesuaian data dan siap untuk dianalisis lebih lanjut.
"""

# Membaca dataset dari file CSV yang diambil dari Kaggle
DFR = pd.read_csv('/content/marketing_campaign.csv', sep='\t') # Use sep='\t' to correctly parse the file

# Menampilkan beberapa baris pertama untuk melihat struktur data dalam dataframe
DFR.head()

"""# **4. Exploratory Data Analysis (EDA)**

Pada tahap ini, Anda akan melakukan **Exploratory Data Analysis (EDA)** untuk memahami karakteristik dataset. EDA bertujuan untuk:

1. **Memahami Struktur Data**
   - Tinjau jumlah baris dan kolom dalam dataset.  
   - Tinjau jenis data di setiap kolom (numerikal atau kategorikal).

2. **Menangani Data yang Hilang**  
   - Identifikasi dan analisis data yang hilang (*missing values*). Tentukan langkah-langkah yang diperlukan untuk menangani data yang hilang, seperti pengisian atau penghapusan data tersebut.

3. **Analisis Distribusi dan Korelasi**  
   - Analisis distribusi variabel numerik dengan statistik deskriptif dan visualisasi seperti histogram atau boxplot.  
   - Periksa hubungan antara variabel menggunakan matriks korelasi atau scatter plot.

4. **Visualisasi Data**  
   - Buat visualisasi dasar seperti grafik distribusi dan diagram batang untuk variabel kategorikal.  
   - Gunakan heatmap atau pairplot untuk menganalisis korelasi antar variabel.

Tujuan dari EDA adalah untuk memperoleh wawasan awal yang mendalam mengenai data dan menentukan langkah selanjutnya dalam analisis atau pemodelan.
"""

# Memilih hanya kolom numerik untuk analisis
numerical_features = DFR.select_dtypes(include=[np.number])

# Menampilkan statistik deskriptif untuk variabel numerik
print("\nStatistik deskriptif untuk variabel numerik:")
print(numerical_features.describe())


# Visualisasi histogram untuk distribusi setiap variabel numerik
numerical_features.hist(figsize=(12, 12), bins=20)
plt.suptitle('Histogram Variabel Numerik', fontsize=16)
plt.show()

# Visualisasi variabel kategorikal
# Education
plt.figure(figsize=(10, 6))
sns.countplot(x='Education', data=DFR, palette='pastel')
plt.xticks(rotation=45)
plt.title('Distribusi Education')
plt.show()

# Marital_Status
plt.figure(figsize=(10, 6))
sns.countplot(x='Marital_Status', data=DFR, palette='pastel')
plt.xticks(rotation=45)
plt.title('Distribusi Marital_Status')
plt.show()

# Analisis korelasi antar variabel numerik
# Menghitung matriks korelasi
correlation_matrix = numerical_features.corr()

# Visualisasi heatmap untuk korelasi antar variabel numerik
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Heatmap Korelasi Variabel Numerik')
plt.show()

"""# **5. Data Preprocessing**

Pada tahap ini, data preprocessing adalah langkah penting untuk memastikan kualitas data sebelum digunakan dalam model machine learning. Data mentah sering kali mengandung nilai kosong, duplikasi, atau rentang nilai yang tidak konsisten, yang dapat memengaruhi kinerja model. Oleh karena itu, proses ini bertujuan untuk membersihkan dan mempersiapkan data agar analisis berjalan optimal.

Berikut adalah tahapan-tahapan yang perlu dilakukan, namun **tidak terbatas** pada:
1. Menghapus atau Menangani Data Kosong (Missing Values)
2. Menghapus Data Duplikat
3. Normalisasi atau Standarisasi Fitur
4. Deteksi dan Penanganan Outlier
5. Encoding Data Kategorikal
6. Binning (Pengelompokan Data)
"""

DFR.dropna(inplace=True)

from sklearn.preprocessing import MinMaxScaler

# Normalisasi pada kolom numerik
scaler = MinMaxScaler()
numerical_cols = DFR.select_dtypes(include=np.number).columns
DFR[numerical_cols] = scaler.fit_transform(DFR[numerical_cols])


# Melakukan encoding pada kolom kategorikal menggunakan LabelEncoder
label_encoder = LabelEncoder()
categorical_cols = DFR.select_dtypes(exclude=np.number).columns
for col in categorical_cols:
    DFR[col] = label_encoder.fit_transform(DFR[col])

"""# **6. Pembangunan Model Clustering**

## **a. Pembangunan Model Clustering**

Pada tahap ini, Anda membangun model clustering dengan memilih algoritma yang sesuai untuk mengelompokkan data berdasarkan kesamaan. Berikut adalah **rekomendasi** tahapannya.
1. Pilih algoritma clustering yang sesuai.
2. Latih model dengan data menggunakan algoritma tersebut.
"""

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 1. Reduksi Dimensi dengan PCA
print("Mereduksi dimensi menjadi 2 komponen utama dengan PCA.")
pca = PCA(n_components=2, random_state=42)  # Add random_state for reproducibility
DFR_pca = pca.fit_transform(DFR)

# 3. Latih Model KMeans
print("Melatih model KMeans dengan jumlah kluster yang telah ditentukan.")
n_clusters = 3  # Update based on optimal cluster analysis
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
kmeans.fit(DFR_pca)

# 4. Tambahkan Label Kluster ke Dataset
print("Menambahkan label kluster ke dataset.")
DFR['cluster'] = kmeans.labels_

# 5. Evaluasi Silhouette Score
silhouette_avg = silhouette_score(DFR_pca, kmeans.labels_)
print(f"Silhouette Score untuk {n_clusters} kluster = {silhouette_avg:.4f}")

"""## **b. Evaluasi Model Clustering**

Untuk menentukan jumlah cluster yang optimal dalam model clustering, Anda dapat menggunakan metode Elbow atau Silhouette Score.

Metode ini membantu kita menemukan jumlah cluster yang memberikan pemisahan terbaik antar kelompok data, sehingga model yang dibangun dapat lebih efektif. Berikut adalah **rekomendasi** tahapannya.
1. Gunakan Silhouette Score dan Elbow Method untuk menentukan jumlah cluster optimal.
2. Hitung Silhouette Score sebagai ukuran kualitas cluster.
"""

from sklearn.decomposition import PCA

# Reduksi dimensi menjadi 2 komponen utama
pca = PCA(n_components=2)
DFR_pca = pca.fit_transform(DFR)

# Evaluasi ulang dengan PCA
inertia_pca = []
silhouette_scores_pca = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(DFR_pca)
    inertia_pca.append(kmeans.inertia_)
    silhouette_scores_pca.append(silhouette_score(DFR_pca, kmeans.labels_))

# Visualisasi Elbow Method setelah PCA
plt.figure(figsize=(8, 6))
plt.plot(range(2, 11), inertia_pca, marker='o')
plt.title('Elbow Method (Setelah PCA)')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()

# Visualisasi Silhouette Score setelah PCA
plt.figure(figsize=(8, 6))
plt.plot(range(2, 11), silhouette_scores_pca, marker='o', color='orange')
plt.title('Silhouette Score (Setelah PCA)')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.show()

# Menampilkan Silhouette Score setelah PCA
print("Silhouette Scores Setelah PCA:")
for k, score in zip(range(2, 11), silhouette_scores_pca):
    print(f"Jumlah Kluster = {k}, Silhouette Score = {score:.4f}")

"""Disini saya menggunakan hanya 3 kluster saja, dengan Silhouette Score = 0.5826

## **c. Feature Selection (Opsional)**

Silakan lakukan feature selection jika Anda membutuhkan optimasi model clustering. Jika Anda menerapkan proses ini, silakan lakukan pemodelan dan evaluasi kembali menggunakan kolom-kolom hasil feature selection. Terakhir, bandingkan hasil performa model sebelum dan sesudah menerapkan feature selection.
"""



"""## **d. Visualisasi Hasil Clustering**

Setelah model clustering dilatih dan jumlah cluster optimal ditentukan, langkah selanjutnya adalah menampilkan hasil clustering melalui visualisasi.

Berikut adalah **rekomendasi** tahapannya.
1. Tampilkan hasil clustering dalam bentuk visualisasi, seperti grafik scatter plot atau 2D PCA projection.
"""

# Visualisasi hasil clustering dengan 2D PCA
PCA = PCA(n_components=2)

# Use all columns of DFR for PCA
HasilPCA = PCA.fit_transform(DFR.drop(columns=['cluster']))

plt.figure(figsize=(8, 6))
plt.scatter(HasilPCA[:, 0], HasilPCA[:, 1], c=DFR['cluster'], cmap='viridis')
plt.title('Hasil Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Cluster')
plt.show()

"""## **e. Analisis dan Interpretasi Hasil Cluster**

Setelah melakukan clustering, langkah selanjutnya adalah menganalisis karakteristik dari masing-masing cluster berdasarkan fitur yang tersedia.

Berikut adalah **rekomendasi** tahapannya.
1. Analisis karakteristik tiap cluster berdasarkan fitur yang tersedia (misalnya, distribusi nilai dalam cluster).
2. Berikan interpretasi: Apakah hasil clustering sesuai dengan ekspektasi dan logika bisnis? Apakah ada pola tertentu yang bisa dimanfaatkan?
"""

DFR_asli = pd.read_csv('/content/marketing_campaign.csv', sep='\t')

DFR_asli['cluster'] = DFR['cluster']

# Menampilkan karakteristik tiap cluster
print("Interpretasi Cluster:")

# Assuming best_k should be the number of clusters (3 in your previous code)
best_k = 3  # Define best_k with the intended value

for cluster in range(best_k):  # best_k adalah jumlah cluster optimal (3 dalam kasus Anda)
    cluster_data = DFR_asli[DFR_asli['cluster'] == cluster]
    print(f"\nCluster {cluster}:")

    # Analisis data kategorikal
    for col in categorical_cols:  # categorical_cols adalah list kolom kategorikal
        print(f"- {col}:")
        print(cluster_data[col].value_counts(normalize=True))  # Menampilkan distribusi kategori

    # Analisis data numerik
    for col in numerical_cols:  # numerical_cols adalah list kolom numerik
        print(f"- {col}:")
        print(f"  Rata-rata: {cluster_data[col].mean():.2f}")
        print(f"  Standar Deviasi: {cluster_data[col].std():.2f}")

"""Tulis hasil interpretasinya di sini.
1. Cluster 0:
- Year_Birth:
  Rata-rata: 1969.08
  Standar Deviasi: 12.10
- Income:
  Rata-rata: 53599.06
  Standar Deviasi: 32336.79
- Recency:
  Rata-rata: 49.14
  Standar Deviasi: 29.26
- Complain:
  Rata-rata: 0.01
  Standar Deviasi: 0.10
- Response:
  Rata-rata: 0.16
  Standar Deviasi: 0.37

Cluster 0 dapat diidentifikasi sebagai kelompok pelanggan paruh baya dengan pendapatan menengah yang baru-baru ini melakukan pembelian. Mereka cenderung puas dengan produk atau layanan yang diterima dan cukup responsif terhadap kampanye pemasaran. Namun, adanya variasi pendapatan yang signifikan dalam cluster ini menunjukkan perlunya segmentasi lebih lanjut berdasarkan tingkat pendapatan untuk merancang strategi pemasaran yang lebih tepat sasaran dan efektif.


---


2. Cluster 1:
- Year_Birth:
  Rata-rata: 1968.79
  Standar Deviasi: 12.09
- Income:
  Rata-rata: 52234.41
  Standar Deviasi: 21296.09
- Recency:
  Rata-rata: 50.98
  Standar Deviasi: 29.60
- Complain:
  Rata-rata: 0.01
  Standar Deviasi: 0.08
- Response:
  Rata-rata: 0.14
  Standar Deviasi: 0.35

Cluster 1 terdiri dari pelanggan paruh baya dengan pendapatan menengah dan tingkat variasi pendapatan yang lebih rendah dibandingkan Cluster 0. Meskipun aktivitas pembelian mereka cenderung lebih rendah dan respons terhadap kampanye pemasaran tidak terlalu signifikan, mereka tetap menunjukkan tingkat kepuasan yang tinggi terhadap produk atau layanan yang diterima.


---

3. Cluster 2:
- Year_Birth:
  Rata-rata: 1968.61
  Standar Deviasi: 11.79
- Income:
  Rata-rata: 50987.07
  Standar Deviasi: 20389.34
- Recency:
  Rata-rata: 47.02
  Standar Deviasi: 27.91
- Complain:
  Rata-rata: 0.01
  Standar Deviasi: 0.11
- Response:
  Rata-rata: 0.15
  Standar Deviasi: 0.36


Cluster 2 terdiri dari pelanggan paruh baya dengan pendapatan menengah ke bawah dan tingkat variabilitas pendapatan yang relatif stabil. Meski memiliki pendapatan lebih rendah, mereka merupakan pelanggan yang paling aktif dalam melakukan pembelian baru-baru ini dan cukup responsif terhadap kampanye pemasaran. Tingkat kepuasan mereka juga sebanding dengan cluster lainnya, menunjukkan kepuasan yang tinggi terhadap produk atau layanan yang diterima.

---

# **7. Mengeksport Data**

Simpan hasilnya ke dalam file CSV.
"""

# Mengekspor hasil clustering ke dalam file CSV
output_path = 'Hasil_Clustering_Cuy.csv'
DFR.to_csv(output_path, index=False)
print(f"Hasil clustering diekspor ke {output_path}")
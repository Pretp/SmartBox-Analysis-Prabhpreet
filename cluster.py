import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Load the login data
file_path = "/Users/prabhpreet16/Desktop/aparna-assignment/School_Login_Data.xlsx"  # Update with the actual file path
df = pd.read_excel(file_path)
# Ensure 'Login Date' is a datetime column
df['Login Date'] = pd.to_datetime(df['Login Date'], format='%d/%m/%y')

# Aggregate login counts per school
grouped = df.groupby('School_Code').size().reset_index(name='Login Count')

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(grouped[['Login Count']])

# Try k=3 and k=4 for clustering
for k in [3, 4]:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    grouped[f'Cluster_{k}'] = kmeans.fit_predict(X_scaled)
    silhouette_avg = silhouette_score(X_scaled, grouped[f'Cluster_{k}'])
    print(f"Silhouette Score for k={k}: {silhouette_avg:.4f}")

    # Visualize clusters with a scatter plot
    plt.figure(figsize=(8, 5))
    plt.scatter(grouped['School_Code'], grouped['Login Count'], c=grouped[f'Cluster_{k}'], cmap='viridis', edgecolors='k')
    plt.xticks(rotation=90)  # Rotate school codes for better readability
    plt.xlabel('School_Code')
    plt.ylabel('Login Count (Standardized)')
    plt.title(f'K-Means Clustering (k={k})')
    plt.colorbar(label='Cluster')
    plt.show()

# Print cluster assignments
print(grouped[['School_Code', 'Login Count', 'Cluster_3', 'Cluster_4']])
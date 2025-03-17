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

# Run K-Means clustering
k = 4  # Using k=4 based on your last visualization
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
grouped['Cluster'] = kmeans.fit_predict(X_scaled)

# Assign colors based on clusters
cluster_colors = {
    0: "dark purple",
    1: "blue",
    2: "green",
    3: "yellow"
}
grouped['colour'] = grouped['Cluster'].map(cluster_colors)

# Load Merged_Data
merged_file_path = "Merged_Data.xlsx"  # Change to actual path
Merged_Data = pd.read_excel(merged_file_path)

# Merge cluster info into Merged_Data
Merged_Data = Merged_Data.merge(grouped[['School_Code', 'colour']], on='School_Code', how='left')

# Save the updated dataset as an Excel file
Merged_Data.to_excel("Merged_Data_with_Clusters.xlsx", index=False)
print("Updated Merged_Data saved as 'Merged_Data_with_Clusters.xlsx'")

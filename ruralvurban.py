import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the dataset
merged_df = pd.read_excel("/Users/prabhpreet16/Desktop/aparna-assignment/Merged_Data.xlsx")

# Split into Rural and Urban schools
rural_schools = merged_df[merged_df["Rural/Urban"] == "Rural"]
urban_schools = merged_df[merged_df["Rural/Urban"] == "Urban"]

# Compute correlation for Rural schools
rural_corr, rural_p = pearsonr(rural_schools["Student_Teacher_Ratio"], rural_schools["Login_Per_Student"])

# Compute correlation for Urban schools
urban_corr, urban_p = pearsonr(urban_schools["Student_Teacher_Ratio"], urban_schools["Login_Per_Student"])

# Print results
print("Rural Schools:")
print(f" Pearson Correlation: {rural_corr:.3f}, P-value: {rural_p:.3f}")
print("\nUrban Schools:")
print(f" Pearson Correlation: {urban_corr:.3f}, P-value: {urban_p:.3f}")

# Scatter plot for Rural Schools
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(x=rural_schools["Student_Teacher_Ratio"], y=rural_schools["Login_Per_Student"], alpha=0.7)
plt.xlabel("Student-Teacher Ratio (Rural)")
plt.ylabel("Login Density")
plt.title(f"Rural Schools: STR vs. SmartBox Usage (r={rural_corr:.3f})")
plt.grid(True)

# Scatter plot for Urban Schools
plt.subplot(1, 2, 2)
sns.scatterplot(x=urban_schools["Student_Teacher_Ratio"], y=urban_schools["Login_Per_Student"], alpha=0.7)
plt.xlabel

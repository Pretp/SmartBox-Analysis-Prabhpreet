import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the dataset
merged_df = pd.read_excel("/Users/prabhpreet16/Desktop/aparna-assignment/Merged_Data.xlsx")

# Remove the outlier: iLearn NGO Centre
filtered_df = merged_df[merged_df["Type of School"] != "iLearn NGO Centre"]

# Split into Rural and Urban schools
rural_schools = filtered_df[filtered_df["Rural/Urban"] == "Rural"]
urban_schools = filtered_df[filtered_df["Rural/Urban"] == "Urban"]

# Compute correlation for Rural schools (without outlier)
rural_corr, rural_p = pearsonr(rural_schools["Student_Teacher_Ratio"], rural_schools["Login_Per_Student"])

# Compute correlation for Urban schools (without outlier)
urban_corr, urban_p = pearsonr(urban_schools["Student_Teacher_Ratio"], urban_schools["Login_Per_Student"])

# Print results
print("Rural Schools (Without Outlier):")
print(f" Pearson Correlation: {rural_corr:.3f}, P-value: {rural_p:.3f}")
print("\nUrban Schools (Without Outlier):")
print(f" Pearson Correlation: {urban_corr:.3f}, P-value: {urban_p:.3f}")

# Scatter plot for Rural Schools (Without Outlier)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(x=rural_schools["Student_Teacher_Ratio"], y=rural_schools["Login_Per_Student"], alpha=0.7)
plt.xlabel("Student-Teacher Ratio (Rural)")
plt.ylabel("Login Density")
plt.title(f"Rural Schools (Without Outlier): STR vs. SmartBox Usage (r={rural_corr:.3f})")
plt.grid(True)

# Scatter plot for Urban Schools (Without Outlier)
plt.subplot(1, 2, 2)
sns.scatterplot(x=urban_schools["Student_Teacher_Ratio"], y=urban_schools["Login_Per_Student"], alpha=0.7)
plt.xlabel("Student-Teacher Ratio (Urban)")
plt.ylabel("Login Density")
plt.title(f"Urban Schools (Without Outlier): STR vs. SmartBox Usage (r={urban_corr:.3f})")
plt.grid(True)

plt.tight_layout()
plt.show()

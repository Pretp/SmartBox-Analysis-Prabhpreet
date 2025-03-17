import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the dataset
merged_df = pd.read_excel("/Users/prabhpreet16/Desktop/aparna-assignment/Merged_Data.xlsx")

# Separate iLearn NGO Centre for comparison
ilearn_df = merged_df[merged_df["Type of School"] == "iLearn NGO Centre"]
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

# Compare iLearn's Login Density with others
ilearn_login_density = ilearn_df["Login_Per_Student"].mean()
rural_avg_login_density = rural_schools["Login_Per_Student"].mean()
urban_avg_login_density = urban_schools["Login_Per_Student"].mean()

print("\nLogin Density Comparison:")
print(f" iLearn NGO Centre: {ilearn_login_density:.3f}")
print(f" Rural Schools (Avg): {rural_avg_login_density:.3f}")
print(f" Urban Schools (Avg): {urban_avg_login_density:.3f}")

# Visualize login density comparison
plt.figure(figsize=(8, 5))
sns.barplot(x=["iLearn NGO Centre", "Rural Schools (Avg)", "Urban Schools (Avg)"], 
            y=[ilearn_login_density, rural_avg_login_density, urban_avg_login_density], 
            palette=["red", "blue", "green"])
plt.ylabel("Average Login Density")
plt.title("Login Density Comparison: iLearn vs. Other Schools")
plt.show()

def detect_outliers(df, columns):
    """Function to detect outliers using IQR method."""
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        print(f"\nOutliers detected in {column}:")
        print(outliers[["Name of School", column]])
        
detect_outliers(merged_df, ["Student_Teacher_Ratio", "Login_Per_Student", "Fees per student in class 6 (Monthly)",
                             "Number of students in class 6", "Number of students in class 7", "Number of Teachers Trained"])

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr

# Load merged dataset
merged_df = pd.read_excel("/Users/prabhpreet16/Desktop/aparna-assignment/Merged_Data.xlsx"
)

# Scatter plot: Student-Teacher Ratio vs. Login Density
plt.figure(figsize=(8, 6))
sns.scatterplot(x=merged_df["Student_Teacher_Ratio"], y=merged_df["Login_Per_Student"], alpha=0.7)
plt.xlabel("Student-Teacher Ratio (Students per Trained Teacher)")
plt.ylabel("Login Density (Logins per SmartBox Student)")
plt.title("SmartBox Usage vs. Teacher Training")
plt.grid(True)
plt.show()

# Compute correlation
corr, p_value = pearsonr(merged_df["Student_Teacher_Ratio"], merged_df["Login_Per_Student"])

print(f"Pearson Correlation Coefficient: {corr:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpretation
if abs(corr) > 0.5:
    print("Strong relationship detected.")
elif abs(corr) > 0.2:
    print("Moderate relationship detected.")
else:
    print("Weak or no relationship detected.")

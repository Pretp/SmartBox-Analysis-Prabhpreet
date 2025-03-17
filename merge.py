import pandas as pd

# File paths (update these with actual file paths)
school_profile_path = "/Users/prabhpreet16/Desktop/aparna-assignment/School_Profile_Data.xlsx"
school_login_path = "/Users/prabhpreet16/Desktop/aparna-assignment/School_Login_Data.xlsx"
output_path = "/Users/prabhpreet16/Desktop/aparna-assignment/Merged_Data.xlsx"

# Load the datasets
school_profile_df = pd.read_excel(school_profile_path)
school_login_df = pd.read_excel(school_login_path)

# Aggregate login counts per school
login_counts = school_login_df.groupby("School_Code").size().reset_index(name="Login_Count")

# Merge datasets on 'School_Code'
merged_df = pd.merge(school_profile_df, login_counts, on="School_Code", how="left")

# Fill missing login counts with 0
merged_df["Login_Count"] = merged_df["Login_Count"].fillna(0).astype(int)

# Determine the number of students using SmartBox
def get_smartbox_students(row):
    if row["Class with SmartBox"] == "6th":
        return row["Number of students in class 6"]
    elif row["Class with SmartBox"] == "7th":
        return row["Number of students in class 7"]
    elif row["Class with SmartBox"] == "Both 6th and 7th":
        return row["Number of students in class 6"] + row["Number of students in class 7"]
    else:
        return 0  # If SmartBox is not assigned, assume 0 students

# Apply the function to compute smartbox student count
merged_df["SmartBox_Students"] = merged_df.apply(get_smartbox_students, axis=1)

# Calculate Login Density (logins per student using SmartBox)
merged_df["Login_Per_Student"] = merged_df["Login_Count"] / merged_df["SmartBox_Students"]
merged_df["Login_Per_Student"] = merged_df["Login_Per_Student"].fillna(0)  # ✅ Safe for future versions

merged_df["Student_Teacher_Ratio"] = merged_df["SmartBox_Students"] / merged_df["Number of Teachers Trained"]
merged_df["Student_Teacher_Ratio"] = merged_df["Student_Teacher_Ratio"].replace([float('inf'), -float('inf')], 0)  # Handle division by zero
merged_df["Student_Teacher_Ratio"] = merged_df["Student_Teacher_Ratio"].fillna(0)  # Handle NaNs

# Save the merged dataset
with pd.ExcelWriter(output_path) as writer:
    merged_df.to_excel(writer, index=False, sheet_name="Merged Data")

print(f"Merged dataset with SmartBox-based login density saved to {output_path}")






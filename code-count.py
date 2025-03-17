import pandas as pd
import matplotlib.pyplot as plt

def count_codes(file, code_column):
    # Read the spreadsheet
    df = pd.read_excel(file)
    print(df.columns)  # Print all column names
    
    # Count occurrences of each code
    code_counts = df[code_column].value_counts()
    
    # Plot the bar chart
    plt.figure(figsize=(12, 6))
    code_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel("Codes")
    plt.ylabel("Frequency")
    plt.title("Code Occurrences")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    return code_counts

# Example usage
file = "/Users/prabhpreet16/Desktop/aparna-assignment/School_Login_Data.xlsx"
code_column = "School Code"  # Replace with the actual column name



code_counts = count_codes(file, code_column)
print(code_counts)

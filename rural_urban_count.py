import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "/Users/prabhpreet16/Desktop/aparna-assignment/Merged_Data.xlsx"  # Replace with your actual file name
df = pd.read_excel(file_path)

# Count the occurrences of "Rural" and "Urban"
counts = df["Rural/Urban"].value_counts()

colors = ["#FF4500", "#B22222"]  # Darker red for better contrast

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    counts, 
    labels=counts.index, 
    autopct='%1.1f%%', 
    colors=colors, 
    startangle=90,
    textprops={'fontsize': 16}  # Increase font size for labels and percentages
)


# Remove borders and background
plt.axis("off")

# Save the image
plt.savefig("rural_urban_pie_chart.png", bbox_inches='tight', transparent=True)
plt.show()

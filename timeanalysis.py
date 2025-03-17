import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load login data
file_path = "/Users/prabhpreet16/Desktop/aparna-assignment/School_Login_Data.xlsx"  # Update with actual path
login_df = pd.read_excel(file_path)

# Convert 'Login Date' to datetime format
login_df['Login Date'] = pd.to_datetime(login_df['Login Date'], format='%d/%m/%y')

# Aggregate logins per day
daily_logins = login_df.groupby('Login Date').size()

# Plot overall login trend
daily_logins.plot(figsize=(12, 6), title='Overall Daily Login Trends', xlabel='Date', ylabel='Number of Logins')
plt.grid()
plt.show()

# Aggregate logins per school per day
school_daily_logins = login_df.groupby(['Login Date', 'School_Code']).size().unstack()

# Heatmap of logins per school
plt.figure(figsize=(12, 6))
sns.heatmap(school_daily_logins.T, cmap='coolwarm', cbar=True, linewidths=0.5)
plt.title("Login Activity per School Over Time")
plt.xlabel("Date")
plt.ylabel("School Code")
plt.show()

# Aggregate logins by weekday
login_df['Weekday'] = login_df['Login Date'].dt.day_name()
weekday_logins = login_df.groupby('Weekday').size()

# Reorder weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_logins = weekday_logins.reindex(weekday_order)

# Plot weekday trends
plt.figure(figsize=(10, 5))
sns.barplot(x=weekday_logins.index, y=weekday_logins.values, palette='viridis')
plt.title("Average Logins by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Number of Logins")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('student_data.csv')

# Add pass/fail status
df['Status'] = df['Grade'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# Summary statistics
average_grade = df['Grade'].mean()
max_grade = df['Grade'].max()
min_grade = df['Grade'].min()
average_attendance = df['Attendance (%)'].mean()

pass_count = df['Status'].value_counts().get('Pass', 0)
fail_count = df['Status'].value_counts().get('Fail', 0)

# Print summary
print(f"Average Grade: {average_grade:.2f}")
print(f"Highest Grade: {max_grade}")
print(f"Lowest Grade: {min_grade}")
print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Pass Count: {pass_count}")
print(f"Fail Count: {fail_count}")

# Bar chart: Pass vs Fail
plt.figure(figsize=(6, 4))
plt.bar(['Pass', 'Fail'], [pass_count, fail_count], color=['green', 'red'])
plt.title('Pass vs Fail Count')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('pass_fail_bar_chart_custom.png')
plt.close()

# Pie chart: Pass/Fail Distribution
plt.figure(figsize=(6, 6))
plt.pie([pass_count, fail_count], labels=['Pass', 'Fail'], autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Pass/Fail Distribution')
plt.tight_layout()
plt.savefig('pass_fail_pie_chart_custom.png')
plt.close()

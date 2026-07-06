import pandas as pd

# Read CSV File
df = pd.read_csv("students.csv")

print("Original Dataset:\n")
print(df)

# Remove Null Values
df = df.dropna()

print("\nDataset after Removing Null Values:\n")
print(df)

# Count Records
count = len(df)

print("\nTotal Records:", count)

# Generate Summary Statistics
print("\nSummary Statistics:\n")
print(df.describe())
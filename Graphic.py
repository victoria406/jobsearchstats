import pandas as pd
import matplotlib.pyplot as plt

file_path = "jobsrchspring.xlsx"

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path, header=None)

third_column_values = df.iloc[:, 2]

# Count the occurrences of each unique value in the third column, including NaN
value_counts = third_column_values.value_counts(dropna=False)

# Filter out NaN from the value counts
value_counts_filtered = value_counts.dropna()

# Plotting
plt.figure(figsize=(10, 6))

# Plotting bar plot
value_counts_filtered.plot(kind='bar', color='skyblue')

# Adding title and labels
plt.title('Distribution of Application Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')

# Set y-axis ticks to include all numbers with an increment of 2
max_count = value_counts_filtered.max()
plt.yticks(range(0, max_count + 1, 2))

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Print the count of "Rejected" values
rejected_count = df[df.iloc[:, 2] == "Rejected"].shape[0]
print("Number of rejections:", rejected_count)

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

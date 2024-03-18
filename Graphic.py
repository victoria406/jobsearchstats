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

# Calculate the total number of applications
total_applications = len(third_column_values)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting bar plot
value_counts_filtered.plot(kind='bar', color='skyblue')

# Adding a bar for total applications
plt.bar("Total Applications", total_applications, color='lightgreen', alpha=0.7)

# Adding title and labels
plt.title('Distribution of Application Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')

# Set y-axis ticks to count by 5s and include the total number
max_count = value_counts_filtered.max()
yticks_range = list(range(0, max_count + 1, 5)) + [total_applications]
plt.yticks(yticks_range)

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
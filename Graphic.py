import pandas as pd
import matplotlib.pyplot as plt


#This is a personal project. After I had applied to
# 79 job postings, I was surprised by the rate at which I was
# being ghosted. That being said, I will admit that at times I lost track
# of my application status, and some employers may still be overviewing my application.
# Therefore, ghosted in the scope of this project are companies that I have applied to which I
# never heard back from as of now (03/18). I will update my csv if I hear back

#author @Victoria White

#the data was also edited for anonymity

file_path = "jobsrchspringOne.xlsx"

df = pd.read_excel(file_path, header=None)

third_column_values = df.iloc[:, 2]

value_counts = third_column_values.value_counts(dropna=False)

value_counts_filtered = value_counts.dropna()

total_applications = len(third_column_values)

plt.figure(figsize=(10, 6))

value_counts_filtered.plot(kind='bar', color='skyblue')

plt.bar("Total Applications", total_applications, color='lightgreen', alpha=0.7)

plt.title('Distribution of Application Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')

max_count = value_counts_filtered.max()
yticks_range = list(range(0, max_count + 1, 5)) + [total_applications]
plt.yticks(yticks_range)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
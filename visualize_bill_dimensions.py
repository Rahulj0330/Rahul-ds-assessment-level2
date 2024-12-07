import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


cleaned_file = "../output/cleaned_data.csv"

data = pd.read_csv(cleaned_file)

plt.figure(figsize=(12, 10))

plt.subplot(3, 3, 1)
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', data=data, hue='species')
plt.title('Scatter Plot: bill_length_mm vs bill_depth_mm')


plt.subplot(3, 3, 2)
sns.lineplot(x='bill_length_mm', y='bill_depth_mm', data=data, hue='species')
plt.title('Line Plot: bill_length_mm vs bill_depth_mm')

plt.subplot(3, 3, 3)
sns.histplot(data['bill_length_mm'], kde=True, color='blue')
plt.title('Histogram: bill_length_mm')



plt.subplot(3, 3, 4)
sns.histplot(data['bill_depth_mm'], kde=True, color='green')
plt.title('Histogram: bill_depth_mm')


plt.subplot(3, 3, 5)
sns.boxplot(x='species', y='bill_length_mm', data=data)
plt.title('Box Plot: bill_length_mm by species')


plt.subplot(3, 3, 6)
sns.boxplot(x='species', y='bill_depth_mm', data=data)
plt.title('Box Plot: bill_depth_mm by species')


plt.subplot(3, 3, 7)
correlation_matrix = data[['bill_length_mm', 'bill_depth_mm']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True)
plt.title('Heatmap: Correlation between bill_length_mm and bill_depth_mm')

plt.tight_layout()
plt.show()

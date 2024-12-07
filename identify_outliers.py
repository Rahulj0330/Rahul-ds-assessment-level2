import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
cleaned_file = "../output/cleaned_data.csv"
data = pd.read_csv(cleaned_file)
numeric_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
outliers_iqr = {}
for column in numeric_columns:
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    
    outliers_iqr[column] = data[(data[column] < lower_bound) | (data[column] > upper_bound)]

   
    print(f"\nOutliers in {column} (IQR method):")
    print(outliers_iqr[column])


outliers_zscore = {}
for column in numeric_columns:
    z_scores = zscore(data[column])
    outliers_zscore[column] = data[(z_scores > 3) | (z_scores < -3)]
    
    
    print(f"\nOutliers in {column} (Z-score method):")
    print(outliers_zscore[column])


plt.figure(figsize=(10, 6))
sns.boxplot(data=data[numeric_columns])
plt.title('Outliers in Numeric Features (IQR & Z-Score)')
plt.tight_layout()
plt.show()

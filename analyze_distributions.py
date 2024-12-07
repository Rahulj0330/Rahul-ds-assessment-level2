import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
cleaned_file = "../output/cleaned_data.csv"
data = pd.read_csv(cleaned_file)
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.histplot(data=data, x='bill_length_mm', hue='species', multiple="stack", kde=True, ax=axes[0])
axes[0].set_title('Distribution of Bill Length (mm) by Species')
sns.histplot(data=data, x='bill_depth_mm', hue='species', multiple="stack", kde=True, ax=axes[1])
axes[1].set_title('Distribution of Bill Depth (mm) by Species')
plt.tight_layout()
plt.show()
for feature in ['bill_length_mm', 'bill_depth_mm']:
    print(f"\n{feature} Analysis:")
    
    for species in data['species'].unique():
        species_data = data[data['species'] == species][feature]
        skewness = skew(species_data)
        kurt = kurtosis(species_data)
        
        print(f"{species}: Skewness = {skewness:.2f}, Kurtosis = {kurt:.2f}")

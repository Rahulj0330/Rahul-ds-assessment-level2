import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns 


cleaned_file = "../output/cleaned_data.csv"


data = pd.read_csv(cleaned_file)

numeric_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']


scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numeric_columns])


pca = PCA()
pca_result = pca.fit_transform(scaled_data)


explained_variance = pca.explained_variance_ratio_


print("Explained variance ratio for each principal component:")
print(explained_variance)


plt.figure(figsize=(8, 5))
plt.bar(range(1, len(explained_variance) + 1), explained_variance)
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio of Principal Components')
plt.tight_layout()
plt.show()


cumulative_variance = explained_variance.cumsum()


plt.figure(figsize=(8, 5))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.xlabel('Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance')
plt.tight_layout()
plt.show()


pca_2d = PCA(n_components=2)
reduced_data = pca_2d.fit_transform(scaled_data)


reduced_df = pd.DataFrame(reduced_data, columns=['PC1', 'PC2'])
reduced_df['species'] = data['species']

plt.figure(figsize=(8, 5))
sns.scatterplot(x='PC1', y='PC2', hue='species', data=reduced_df, palette='Set2')
plt.title('PCA - 2D Representation of Data')
plt.tight_layout()
plt.show()

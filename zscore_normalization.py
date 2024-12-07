import pandas as pd
from scipy.stats import zscore

cleaned_file = "../output/cleaned_data.csv"


data = pd.read_csv(cleaned_file)

numerical_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
data[numerical_columns] = data[numerical_columns].apply(zscore)

normalized_file = "../output/normalized_data.csv"
data.to_csv(normalized_file, index=False)
print(data.head())

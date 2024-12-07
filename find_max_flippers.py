import pandas as pd


cleaned_file = "../output/cleaned_data.csv"


data = pd.read_csv(cleaned_file)


max_flipper_length = data.groupby(['species', 'island'])['flipper_length_mm'].max().reset_index()


print("Maximum flipper_length_mm for each species and island:")
print(max_flipper_length)


longest_flippers = max_flipper_length.loc[max_flipper_length.groupby('island')['flipper_length_mm'].idxmax()]


print("\nSpecies with the longest flippers on each island:")
print(longest_flippers)

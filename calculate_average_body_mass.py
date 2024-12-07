import pandas as pd


cleaned_file = "../output/cleaned_data.csv"

data = pd.read_csv(cleaned_file)
gentoo_data = data[data['species'] == 'Gentoo']

average_body_mass = gentoo_data['body_mass_g'].mean()
print(f"The average body mass for Gentoo penguins is {average_body_mass:.2f} grams.")

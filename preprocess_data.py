import pandas as pd

input_file = "../data/dataset.csv"
output_file = "../output/cleaned_data.csv"


data = pd.read_csv(input_file)


numeric_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())


data['sex'] = data['sex'].fillna(data['sex'].mode()[0])


ranges = {
    'bill_length_mm': (30, 60),
    'bill_depth_mm': (13, 23),
    'flipper_length_mm': (170, 240),
    'body_mass_g': (2500, 6500)
}


incorrect_data = {}
for column, (min_val, max_val) in ranges.items():
    incorrect_values = data[(data[column] < min_val) | (data[column] > max_val)]
    incorrect_data[column] = incorrect_values if not incorrect_values.empty else None

print("Incorrect Data:\n")
for column, values in incorrect_data.items():
    if values is not None:
        print(f"Column: {column}")
        print(values)


data.to_csv(output_file, index=False)
print(f"Cleaned dataset saved to {output_file}")

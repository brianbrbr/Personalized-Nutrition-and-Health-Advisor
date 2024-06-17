import pandas as pd

# Data preprocessing
nutrition_df = pd.read_csv('nutrition_data.csv')
health_df = pd.read_csv('health_data.csv')

nutrition_df.fillna(0, inplace=True)
health_df.fillna(0, inplace=True)

# Merge datasets
data = pd.merge(nutrition_df, health_df, on=['user_id', 'date'])
data.to_csv('preprocessed_data.csv', index=False)

print("Data preprocessing completed and saved to 'preprocessed_data.csv'")

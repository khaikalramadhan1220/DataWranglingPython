import pandas as pd
csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
print(csv_data['Age'].iloc[1])
print("Cuplikan Dataset:")
print(csv_data.head())  

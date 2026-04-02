import pandas as pd

df = pd.read_csv("data/patients_dakar.csv")
print(f"Nombre de patients : {len(df)}")
print(df.head())
print(df["diagnostic"].value_counts())
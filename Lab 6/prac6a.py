import pandas as pd

url = "https://github.com/vizydrop/data-samples/blob/master/flowers.csv"
df = pd.read_csv("flowers.csv")

print(df.info())
print("Total Null Values: ", df.isna().sum().sum())
new_df = df.iloc[:, :-1] 
print("-------->Replacing Null Values with Mean")
new_df.fillna(new_df.iloc[:, :].mean(), inplace=True)
print(new_df.info())
print("-------->Column wise mean")
print(df.iloc[:, :-1].mean())
print("-------->Column wise Median")
print(df.iloc[:, :-1].median())
print("-------->Column wise Standard Deviation")
print(df.iloc[:, :-1].std())
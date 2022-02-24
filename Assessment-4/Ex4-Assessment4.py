import pandas as pd

#df=pd.read_csv("StudentData.csv")
df=pd.read_csv("matches.csv")

print(df.head(5))
print(df.columns)

dw = df.loc[df['win_by_wickets']>0] # to print win_by_wickets row value without nonzero values
print(dw)
print(df.loc[:,"win_by_wickets"].mean()) # to print mean of win_by_wickets column
print(df['win_by_wickets'].std()) # to Print the standard deviation of column win by wickets
print(df.groupby(by="city")["winner"].sum())

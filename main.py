# Data Analysis of Churns on the telecomunications company
import pandas as pd
import plotly.express as px

df = pd.read_csv("telecom_users.csv")

# Printing the dataframe with the .info() option from pandas lib
print("After Data Processing\n")
print(df.info())

# Data processing
df = df.drop("Unnamed: 0", axis="columns")
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
df = df.dropna(how="all", axis="columns")
df = df.dropna(how="any", axis=0)

print("\nBefore Data Processing\n")
print(df.info())

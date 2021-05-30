# Data Analysis of Churns on the telecomunications company
import pandas as pd
import plotly.express as px
import os
from IPython.display import display

# Dataframe from the project
df = pd.read_csv("telecom_users.csv")

# Printing the dataframe with the .info() option from pandas lib
print("After Data Processing\n")
print(df.info())

# Data processing
df = df.drop("Unnamed: 0", axis=1)
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
df = df.dropna(how="all", axis=1)
df = df.dropna(how="any", axis=0)

# Before Data Processing
print("\nBefore Data Processing\n")
print(df.info())

# Checking the percentage of Churns in the Dataframe -> Around 26%
display(df["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Visualizing the data
for column in df:
    grap = px.histogram(df, x=column, color="Churn")
    grap.show()

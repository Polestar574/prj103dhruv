import pandas as pd
import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")

fig = px.scatter(df, x = 'Date', y = "Number of Cases", color = "Country")

fig.show()

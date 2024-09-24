import plotly.express as px
import pandas as pd


df = pd.read_csv('./datasett_oppgave1.csv', delimiter=';', encoding='latin1')

print(df)

print(df.columns.tolist())
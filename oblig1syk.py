import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('./datasett_oppgave2.csv')

print(df['fbs'])

label_encoder = LabelEncoder()

# Automatically transform all categorical columns to numerical values
for column in df.select_dtypes(include=['object']).columns:
    df[column] = label_encoder.fit_transform(df[column])

df['fbs'] = label_encoder.fit_transform(df['fbs'])
df['exang'] = label_encoder.fit_transform(df['exang'])

print(df['fbs'])
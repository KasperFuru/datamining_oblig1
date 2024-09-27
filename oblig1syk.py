import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('./datasett_oppgave2.csv')

label_encoder = LabelEncoder()

# Automatically transform all categorical columns to numerical values
for column in df.select_dtypes(include=['object']).columns:
    df[column] = label_encoder.fit_transform(df[column])

df['fbs'] = label_encoder.fit_transform(df['fbs'])
df['exang'] = label_encoder.fit_transform(df['exang'])

# Create a histogram of the fbs column
plt.figure()
df['fbs'].hist(bins=10, edgecolor='black')
plt.title('Histogram of fbs')
plt.xlabel('fbs')
plt.ylabel('Frequency')
plt.show()

# Create a histogram of the exang column
plt.figure()
df['exang'].hist(bins=10, edgecolor='black')
plt.title('Histogram of exang')
plt.xlabel('axang')
plt.ylabel('Frequency')

plt.show()
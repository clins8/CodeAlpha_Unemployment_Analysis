import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Rename and clean columns
df.columns = ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate', 'Area']
df['Date'] = pd.to_datetime(df['Date'])

# Check missing data
print(df.isnull().sum())

# Plot Unemployment Rate over time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate', hue='Region')
plt.title('Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')
plt.grid()
plt.show()

# Overall trends
region_avg = df.groupby('Region')['Estimated Unemployment Rate'].mean().sort_values()
print("Average Unemployment Rate by Region:\n", region_avg)

# Covid Impact Visualization (2020)
covid_data = df[df['Date'].dt.year == 2020]
plt.figure(figsize=(10,6))
sns.lineplot(data=covid_data, x='Date', y='Estimated Unemployment Rate', hue='Region')
plt.title('Unemployment Trend During 2020 (Covid-19)')
plt.show()

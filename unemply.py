import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load both CSV files
df1 = pd.read_csv(r"D:\book\archive (3)\Unemployment in India.csv", encoding='utf-8-sig')
df2 = pd.read_csv(r"D:\book\archive (3)\Unemployment_Rate_upto_11_2020.csv", encoding='ISO-8859-1')

# Remove unwanted spaces from column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Standardize column names for df1
df1 = df1[['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)',
           'Estimated Employed', 'Estimated Labour Participation Rate (%)', 'Area']]

# For df2: check if 'Area' exists, else add manually
required_columns = ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)',
                    'Estimated Employed', 'Estimated Labour Participation Rate (%)']

# Only keep required columns that exist
df2 = df2[[col for col in required_columns if col in df2.columns]]

# Add 'Area' column manually if missing
if 'Area' not in df2.columns:
    df2['Area'] = 'Unknown'

# Rename both dataframes to standard column names
rename_cols = {
    'Estimated Unemployment Rate (%)': 'Estimated Unemployment Rate',
    'Estimated Labour Participation Rate (%)': 'Estimated Labour Participation Rate'
}
df1.rename(columns=rename_cols, inplace=True)
df2.rename(columns=rename_cols, inplace=True)

# Combine both datasets
df = pd.concat([df1, df2], ignore_index=True)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y', errors='coerce')
df.dropna(subset=['Date'], inplace=True)
df.dropna(inplace=True)

# PLOT 1: Unemployment Over Time by Region
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate', hue='Region')
plt.title('Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

# AVERAGE by Region
region_avg = df.groupby('Region')['Estimated Unemployment Rate'].mean().sort_values()
print("\nAverage Unemployment Rate by Region:\n", region_avg)

# PLOT 2: COVID-19 Year (2020)
covid_df = df[df['Date'].dt.year == 2020]
plt.figure(figsize=(12, 6))
sns.lineplot(data=covid_df, x='Date', y='Estimated Unemployment Rate', hue='Region')
plt.title('Unemployment Trends During 2020 (Covid-19 Impact)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

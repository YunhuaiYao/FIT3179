import pandas as pd

# Load the dataset
df = pd.read_csv('GlobalLandTemperaturesByState.csv')

# Filter for Australia and the required dates
df = df[(df['Country'] == 'Australia') & (df['dt'] >= '1990-01-01') & (df['dt'] <= '2012-12-31')]

# Convert dt to datetime and extract the year
df['dt'] = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year

# Group by State and Year to calculate the mean temperature
annual_temps = df.groupby(['State', 'Year'])['AverageTemperature'].mean().reset_index()

# Save the processed data to a new CSV (optional)
annual_temps.to_csv('annual_avg_temps.csv', index=False)

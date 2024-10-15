import pandas as pd

# Load the CSV file
df = pd.read_csv('annual_avg_temps.csv')

# Pivot the data: move 'Year' to columns and 'AverageTemperature' as values
df_pivot = df.pivot(index='State', columns='Year', values='AverageTemperature')

# Reset index to flatten the DataFrame
df_pivot.reset_index(inplace=True)

# Save the transformed data back to CSV
df_pivot.to_csv('annual_avg_temps_wide.csv', index=False)

print("CSV has been successfully transformed and saved as 'annual_avg_temps_wide.csv'")

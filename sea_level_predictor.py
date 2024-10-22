# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data from file
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Create first line of best fit for all data
slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create x values for predictions from 1880 to 2050
years_extended = pd.Series(range(1880, 2051))
# Calculate y values using the slope and intercept
sea_level_pred_all = intercept_all + slope_all * years_extended

# Plot the line of best fit
plt.plot(years_extended, sea_level_pred_all, 'r', label='Best Fit Line (1880-2050)')

# Create second line of best fit starting from 2000
recent_df = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])

# Create x values for predictions from 2000 to 2050
years_recent = pd.Series(range(2000, 2051))
# Calculate y values for the recent data
sea_level_pred_recent = intercept_recent + slope_recent * years_recent

# Plot the second line of best fit
plt.plot(years_recent, sea_level_pred_recent, 'g', label='Best Fit Line (2000-2050)')

# Add labels and title
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.legend()

# Save plot and return data for testing (Do not modify)
plt.savefig('sea_level_plot.png')
plt.show()

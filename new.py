import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('output4h.csv')

# Convert the 'datetime' column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Set the 'datetime' column as the index
df.set_index('datetime', inplace=True)

# Filter the DataFrame to include only rows where 'signals' is not zero
filtered_df = df[df['signals'] != 0]

# Separate the signals
positive_signals = filtered_df[filtered_df['signals'] == 1]
negative_signals = filtered_df[filtered_df['signals'] == -1]

# Count the number of points for each signal type
num_positive_signals = len(positive_signals)
num_negative_signals = len(negative_signals)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['close'], label='Close Price', alpha=0.5)
plt.scatter(positive_signals.index, positive_signals['close'], color='green', label='+1 Signal Points')
plt.scatter(negative_signals.index, negative_signals['close'], color='red', label='-1 Signal Points')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Close Price Over Time with Signal Points')
plt.legend()
plt.grid(True)

# Display the counts of signal points
plt.figtext(0.15, 0.85, f'+1 Signal Points: {num_positive_signals}', color='green')
plt.figtext(0.15, 0.80, f'-1 Signal Points: {num_negative_signals}', color='red')

plt.show()
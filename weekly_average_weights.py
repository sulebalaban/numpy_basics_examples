import numpy as np

# Daily weight data
dailyweight = [
    185., 184.8, 184.6, 184.4, 184.2, 184., 183.8,
    183.6, 183.4, 183.2, 183., 182.8, 182.6, 182.4,
    182.2, 182., 181.8, 181.6, 181.4, 181.2, 181.,
    180.8, 180.6, 180.4, 180.2, 180., 179.8, 179.6,
    179.4, 179.2, 179., 178.8, 178.6, 178.4, 178.2
]
# Convert list to a numpy array
week = np.array(dailyweight)

# Reshape to have rows of 7 (each week)
weekend = week.reshape(-1, 7)

# Calculate the mean of days 6 and 7 for each week (weekends)
result = weekend[:, 5:7]
print(result.mean(axis=1))
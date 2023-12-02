import pandas as pd

# Load the data
df = pd.read_csv('D:/Programming in Java/weka/dermatology.csv')

# Replace '?' with '0'
df.replace('?', '0', inplace=True)

# Save the processed data
df.to_csv('D:/Programming in Java/weka/dermatology.csv', index=False)
print("Done")
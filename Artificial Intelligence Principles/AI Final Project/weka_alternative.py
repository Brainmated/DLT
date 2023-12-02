import pandas as pd

# Load your CSV file as a single column
df = pd.read_csv('D:/Programming in Java/weka/dermatology.csv', header=None)

# Split each row into separate columns
df = df[0].str.split(',', expand=True)

# Extract the first row to create column headers
columns = df.iloc[0]

# Apply the column headers
df.columns = columns

# Remove the first row (which is now the header)
df = df.iloc[1:]

# Save the DataFrame back to a CSV
df.to_csv('D:/Programming in Java/weka/dermatology.csv', index=False)
print("Done")
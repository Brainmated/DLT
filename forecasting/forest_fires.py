import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.metrics import accuracy_score

directory = "E:/Programming in Python/data" 
data = []  

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.startswith("forest_fires") and filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        data.append(df)

# Concatenate data from multiple files into a single DataFrame
data = pd.concat(data)
print("Data collected and concatenated.")

firefighters = data["ΠΥΡΟΣ. ΣΩΜΑ"].dropna().values
volunteers = data["ΕΘΕΛΟ-ΝΤΕΣ"].dropna().values
army_personnel = data["ΣΤΡΑΤΟΣ"].dropna().values

# Ensure all arrays have the same length
min_length = min(len(firefighters), len(volunteers), len(army_personnel))
firefighters = firefighters[:min_length]
volunteers = volunteers[:min_length]
army_personnel = army_personnel[:min_length]

# Stack the features horizontally
features = np.column_stack((volunteers, army_personnel))

# Assign the label
label = firefighters

model = LinearRegression()
print("Model selected.")

x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=8)

model.fit(x_train, y_train)
print("Model trained, calculating prediction...")

y_pred = model.predict(x_test)

# Get the total number of individuals (firefighters, volunteers, and army personnel) for each data point
total_individuals = np.sum(features, axis=1)

# Get the number of data points
num_data_points = len(y_test)

# Create an array representing the data point indices
indices = np.arange(num_data_points)

# Plotting the predicted values and actual values
plt.figure(figsize=(20, 10))
plt.scatter(indices, y_test, color='blue', label='Actual')
plt.scatter(indices, y_pred, color='red', label='Predicted')
plt.scatter(indices, total_individuals[:num_data_points], color='green', label='Total Individuals')
plt.xlabel('Data Point')
plt.ylabel('Number of Individuals')
plt.title('Actual vs Predicted Firefighters')
plt.legend()
plt.savefig("E:/Programming in Python/results/Graphs/firefighters.png")
print("Graph available at: E:/Programming in Python/results/Graphs/")

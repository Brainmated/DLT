import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

start_time = time.time()
data = pd.read_csv("E:/Programming in Python/data/World_Port_Index.csv", header=1)
print("CSV Read.")

#x and y coordinates in 1st and 2nd column
x_coords = data.iloc[:, 0].values
y_coords = data.iloc[:, 1].values

#coordinates
coords = np.column_stack((x_coords, y_coords))
ports = data["PORT_NAME"]

dist = np.zeros((len(ports), len(ports)))
for i in range(len(ports)):
    for j in range(len(ports)):
        #Haversine Formula
        return "test"
    return "test1"
        

def calculate_distance():
    '''
        Parameters:
        lat1 (float): Latitude of the first point in degrees.
        lon1 (float): Longitude of the first point in degrees.
        lat2 (float): Latitude of the second point in degrees.
        lon2 (float): Longitude of the second point in degrees.
    
        Returns:
        float: Distance between the two points in kilometers.

        LAT_DEG = latitude degrees
        LAT_MIN = latitude minutes
        LAT_HEMI = latitude hemisphere, N and S for the halves of the hemisphere
        LONG_DEG = longitude degrees
        LONG_MIN = longitude minutes
        LONG_HEMI longitude hemisphere, Eastern and Western Hemisphere
        '''
    return 1

plt.scatter(coords[:, 0], coords[:, 1], marker = "o", color = "blue")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.title("Distance between World Ports")

plt.savefig()

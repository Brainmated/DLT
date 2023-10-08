import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time

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
        return 1
        

def calculate_distance():
    '''
        Parameters:
        lat1 (float): Latitude of the first point in degrees.
        lon1 (float): Longitude of the first point in degrees.
        lat2 (float): Latitude of the second point in degrees.
        lon2 (float): Longitude of the second point in degrees.
    
        Returns:
        float: Distance between the two points in kilometers.
        '''
    return 1

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

start_time = time.time()
data = pd.read_csv("D:/Programming in Python/data/World_Port_Index.csv", header=0)
print("CSV Read.")

#x and y coordinates in 1st and 2nd column
x_coords = data.iloc[:, 0].values
y_coords = data.iloc[:, 1].values

#coordinates
coords = np.column_stack((x_coords, y_coords))
ports = data.iloc[:, 3].values

radius = 6371

port1 = input("Enter Port 1: ")
port2 = input("Enter Port 2: ")

if all(port in ports for port in ports[port1, port2]):
    calculate_distance(port1, port2)
else:
    

'''
Before the plot is generated, a gui will be made, asking for user input.

'''
def generate_plot():
    plt.scatter(coords[:, 0], coords[:, 1], marker = "o", color = "blue")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Distance between World Ports")

    plt.savefig()
    return "Plot saved."

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import math

start_time = time.time()
data = pd.read_csv("D:/Programming in Python/data/World_Port_Index.csv", header=0)
end_time = time.time()
total_time = end_time - start_time
print(f"CSV Read in {total_time} seconds.")

latitude = data.iloc[:, 5].values
longitude = data.iloc[:, 6].values

ports = data.iloc[:, 3].values

radius = 6371

port1 = input("Enter Port 1: ")
port2 = input("Enter Port 2: ")

start_time = time.time()
def find_ports():

    latx = None
    lonx = None
    laty = None
    lony = None

    if port1 in ports:
        index1 = ports.tolist().index(port1)
        latx = latitude[index1]
        lonx = longitude[index1]
        print(f"Port {port1} located.")
    else:
        print(f"Port '{port1}' not found in the 'ports' data.")
    
    if port2 in ports:
        index2 = ports.tolist().index(port2)
        laty = latitude[index2]
        lony = longitude[index2]   
        print(f"Port {port2} located.")
    else:
        print(f"Port '{port2}' not found in the 'ports' data.")

    return latx, lonx, laty, lony

def calculate_distance(latx, lonx, laty, lony):

    latx = math.radians(latx)
    lonx = math.radians(lonx)
    laty = math.radians(laty)
    lony = math.radians(lony)

    dlon = lony - lonx
    dlat = latx - laty

    a = math.sin(dlat/2)**2 + math.cos(latx) * math.cos(laty) * math.sin(dlon/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius = 6371

    distance = radius * c

    return distance
    
latx, lonx, laty, lony = find_ports()
end_time = time.time()
total_time = end_time - start_time
if latx is not None and lonx is not None and laty is not None and lony is not None:
    distance = calculate_distance(latx, lonx, laty, lony)
    print(f"The distance between {port1} and {port2} is {distance:.2f} kilometers.")
    print(f"Calculation time: {total_time} seconds")
else:
    print("Cannot calculate the distance. Please verify the input ports.")

'''
def generate_plot():
    plt.scatter(coords[:, 0], coords[:, 1], marker = "o", color = "blue")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Distance between World Ports")

    plt.savefig()
    return "Plot saved."
'''

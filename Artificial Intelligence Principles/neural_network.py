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
print("CSV Read.")

latitude = data.iloc[:, 5].values
longitude = data.iloc[:, 6].values

ports = data.iloc[:, 3].values

radius = 6371

port1 = input("Enter Port 1: ")
port2 = input("Enter Port 2: ")

def find_ports():
    if port1 in ports:
        index1 = ports.index(port1)
        latx = latitude[index1]
        lonx = longitude[index1]
        print(f"Port {port1} located.")
        return latx, lonx
    else:
        print(f"Port '{port1}' not found in the 'ports' data.")
    
    if port2 in ports:
        index2 = ports.index(port2)
        laty = latitude[index2]
        lony = longitude[index2]   
        print(f"Port {port2} located.")
        return laty, lony
    else:
        print(f"Port '{port2}' not found in the 'ports' data.")

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
    


calculate_distance(port1, port2)

'''
def generate_plot():
    plt.scatter(coords[:, 0], coords[:, 1], marker = "o", color = "blue")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Distance between World Ports")

    plt.savefig()
    return "Plot saved."
'''

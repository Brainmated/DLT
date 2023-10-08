import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time

start_time = time.time()
data = pd.read_csv("E:/Programming in Python/data/World_Port_Index.csv", header=1)

x_coords = data.iloc[:, 0].values
y_coords = data.iloc[:, 0].values

coords = np.column_stack((x_coords, y_coords))

end_time = time.time()
comp_time = end_time - start_time
print("Time to read csv: ", comp_time)

import pandas as pd

directory = "E:/data/"

#Range of file names from one to ten, not allowing dynamic indexing yet
start_index = 0
end_index = 10

for i in range(start_index, end_index + 1):
  #itterate each time for fires1.csv, fires2.csv... etc
    file_path = directory + f"fires{i}.csv"
    data = pd.read_csv(file_path)
    
    find_dates()
    montly_occurrences()
    average_extinguish_time()
    test_function()
    
    #Printing filenames and total of rows, can compute later extra features
    filename = f"fires{i}.csv"
    print(f"File: {filename}")
    print(f"Number of rows: {len(data)}")

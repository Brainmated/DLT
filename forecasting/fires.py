import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
# -*- coding: utf-8 -*-

# Read the CSV file
data = pd.read_csv("data/fires.csv")

_id = data["Α/Α Εγγραφής"].values
service = data["Υπηρεσία"].values
prefecture = data["Νομός"].values
event_type = data["Είδος Συμβάντος"].values
date_start = data["Ημερ. Έναρξης Συμβάντος"].values
time_start = data["Ώρα Έναρξης"].values
end_date = data["Ημερ. Κατάσβεσης"]
end_time = data["Ώρα Κατάσβεσης"]
village = data["Χωριό"].values
loc_description = data["Περιγραφή Χώρου"].values
accident_desc = data["Χαρακτηρισμός Συμβάντος"].values
munic = data["Δήμος"].values
total_vehicles = data["Σύνολο Πυρ. Οχημάτων"].values
total_firefighters = data["Σύνολο Πυρ. Δυνάμεων (σε άνδρες και γυναίκες)"].values
total_ships = data["Σύνολο Πυροσβ. Πλοιαρίων"].values

acc_type = data["Τύπος Ατυχήματος"].values
acc_type_np = np.array(acc_type)

interferors_per_type = data["Αριθμός εμπλεκομένων   ανά τύπο "].values
injuries = data["Τραυματίες"].values

casualties = data["Θάνατοι"].values
nonzero_casualties = data[casualties>0]

destructions = data["Καταστροφές"].values
burns = data["Εγκαύματα"].values


fires = ["ΜΙΚΡΗ", "ΜΕΣΑΙΑ", "ΜΕΓΑΛΗ"]

print("All data retrieved!")

def find_dates():
    # Create empty lists to store the found data types and dates
    found_data_types = []
    found_dates = []

    # Iterate over the DataFrame
    for index, row in data.iterrows():
        data_type = row['Χαρακτηρισμός Συμβάντος']
        date = row['Ημερ. Έναρξης Συμβάντος']
        
        # Check if the data type matches one of the desired data types
        if data_type in fires:
            found_data_types.append(data_type)
            found_dates.append(date)

    # Create a new DataFrame with the found data types and dates
    result = pd.DataFrame({
        'Data Type': found_data_types,
        'Date': found_dates
    })

    # Save the result to a CSV file with two separate columns
    result.to_csv('results/reports/result.txt', index=False, encoding='utf-8')

    print("Results are ready")


def monthly_occurences():

    data["Ημερ. Έναρξης Συμβάντος"] = pd.to_datetime(data["Ημερ. Έναρξης Συμβάντος"])
    data["Μήνας"] = data["Ημερ. Έναρξης Συμβάντος"].dt.month
    print("Date okay")

    filtered_data = data[data["Χαρακτηρισμός Συμβάντος"].isin(fires)]
    grouped_data = filtered_data.groupby(["Χαρακτηρισμός Συμβάντος", "Χωριό", "Μήνας"]).size().reset_index(name="Occurrences")
    print("Data filtered and grouped")

    max_occurrences = grouped_data.groupby("Χαρακτηρισμός Συμβάντος")["Occurrences"].idxmax()
    max_occurrences_data = grouped_data.loc[max_occurrences]
    print("Calculated max occurrences")

    for index, row in max_occurrences_data.iterrows():
        accident = row["Χαρακτηρισμός Συμβάντος"]
        location = row["Χωριό"]
        month = pd.to_datetime(row["Μήνας"], format="%m").strftime("%B")
        occurrences = row["Occurrences"]
        print(f"Most occurrences of {accident} happened in {location} during {month}.")
        print(f"Total occurrences: {occurrences}\n")
        label = f"{accident} ({location}) "
        plt.bar(label, occurrences, label=label)
        plt.text(label, occurrences, f"{occurrences}\n{month}", ha='center', va='bottom')


    plt.xlabel('Fires and Locations')
    plt.ylabel('Total Occurrences')
    plt.ylim(0, 150)
    plt.title('Most Occurrences of Fires in Different Locations')
    plt.tight_layout()
    plt.savefig("results/graphs/graph.png")

def average_extinguish_time():
    
    extinguish_times = {}  # Dictionary to store total extinguish times per fire type
    fire_counts = {}  # Dictionary to store counts of each fire type

    for i in range(len(data)):
        # Extract the start date and time from the respective lists and create a datetime object
        start_datetime = datetime.strptime(date_start[i] + " " + time_start[i], "%m/%d/%Y %H:%M")
        
        # Check if the end date and time are strings
        if isinstance(end_date[i], str) and isinstance(end_time[i], str):

            # Extract the end date and time from the respective lists and create a datetime object
            end_datetime = datetime.strptime(str(end_date[i]) + " " + str(end_time[i]), "%m/%d/%Y %H:%M")

            # Calculate the extinguish time as the difference between the end and start datetime
            extinguish_time = end_datetime - start_datetime

            # Get the fire type for the current iteration
            fire_type = accident_desc[i]
            
            if fire_type in fires:
                if fire_type in extinguish_times:
                    # If the fire type already exists in the extinguish_times dictionary, update the total extinguish time and fire count
                    extinguish_times[fire_type] += extinguish_time
                    fire_counts[fire_type] += 1
                else:
                    # If the fire type does not exist in the extinguish_times dictionary, initialize the total extinguish time and fire count
                    extinguish_times[fire_type] = extinguish_time
                    fire_counts[fire_type] = 1
    
    average_extinguish_times = {}

    for fire_type in extinguish_times:
        average_extinguish_times[fire_type] = extinguish_times[fire_type] / fire_counts[fire_type]

    for fire_type in average_extinguish_times:
        print("Average extinguish time for", fire_type, "fire:", average_extinguish_times[fire_type]," from a total of", fire_counts[fire_type], " fires.")
    
average_extinguish_time()

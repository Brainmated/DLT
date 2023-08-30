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
# -*- coding: utf-8 -*-

directory = "/data"  # Replace with the actual path to your directory
data = []  # List to store data from multiple files

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.startswith("region_fires") and filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        data.append(df)

# Concatenate data from multiple files into a single DataFrame
data = pd.concat(data)

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
'''
def damages_reg():
    features = ["Χωριό", "Χαρακτηρισμός Συμβάντος", "Σύνολο Πυρ. Δυνάμεων (σε άνδρες και γυναίκες)", "Σύνολο Πυρ. Οχημάτων"]
    label = ["Καταστροφές"]

    #feature matix x and label matrix y
    x = data[features]
    y = data[label]

    #handle categorical variables such as accident_desc because it's a type
    #perform one-hot encoding 
    x_encoded = pd.get_dummies(x, drop_first=True)

    #split data to training and testing
    x_train, x_test, y_train, y_test = train_test_split(x_encoded, y, test_size=0.2, random_state=8)

    #train the model
    model = LinearRegression()
    model.fit(x_train, y_train)
    
    #make the predictions
    y_pred = model.predict(x_test)

    #evaluate model with mse and r squared
    mse = mean_squared_error(y_test, y_pred) #comparables
    r2 = r2_score(y_test, y_pred)

    print("The Mean Square Error is: ", mse)
    print("The R Squared Score is: ", r2)

damages_reg()
'''
def damages_clustering():
    features = ["Σύνολο Πυρ. Δυνάμεων (σε άνδρες και γυναίκες)", "Σύνολο Πυρ. Οχημάτων", "Καταστροφές", "Τραυματίες"]

    X = data[features]

    # Perform feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform K-means clustering
    k = 3  # Replace with the desired number of clusters
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)

    # Get the cluster assignments for each data point
    cluster_labels = kmeans.labels_

    # Append the cluster labels to the original dataset
    data["Cluster"] = cluster_labels

    # Optional: Print the cluster centroids
    cluster_centers = kmeans.cluster_centers_
    print("Cluster Centers:")
    for i, center in enumerate(cluster_centers):
        print(f"Cluster {i+1}: {center}")

    # Optional: Evaluate the clustering solution
    # You can use evaluation metrics such as silhouette score or within-cluster sum of squares (WCSS)

    # Return the data with cluster labels
    return data

damages_clustering()

'''Cluster Centers:
Cluster 1: [-3.75139890e-03 -5.11211786e-06 -4.11990364e-03  2.73540083e-06]
Cluster 2: [ 5.00952984e-02  6.53479751e-01  2.42724123e+02 -8.05767023e-02]
Cluster 3: [ 2.20959820e+02 -3.52304439e-01 -4.11990364e-03 -8.05767023e-02]
'''

def gradient_boosting():

    x = data.dropna(subset=("Σύνολο Πυρ. Δυνάμεων (σε άνδρες και γυναίκες)", "Αριθμός εμπλεκομένων   ανά τύπο "), axis=1)
    y = data["Θάνατοι"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=8)

    model = xgb.XGBClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

gradient_boosting()

    print(predictions)
    '''

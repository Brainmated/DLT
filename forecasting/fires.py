import pandas as pd
import numpy as np

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

result = np.concat([acc_type, nonzero_casualties], axis=1)


result.to_csv("results/results.csv", index=False)

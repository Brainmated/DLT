import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sn
from sklearn.metrics import classification_report

data = pd.read_csv("data/Iris.csv")

x = data[["PetalLengthCm", "PetalWidthCm"]]
y = data["Species"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2, random_state=8)

k = 3
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

acc = accuracy_score(y_test, y_pred)

#print(f"Accuracy: {int(acc*100)}%")

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10,6))
sn.heatmap(cm, annot=True)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.savefig("results/graphs/heatmap_{}%{}.png".format(int(acc*100), "accuracy"))

# Plot neighbors
plt.figure(figsize=(10, 6))
plt.scatter(x_test["PetalLengthCm"], x_test["PetalWidthCm"], color="green")
plt.scatter(x_train["PetalLengthCm"], x_train["PetalWidthCm"], color="red", marker="x")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("KNN Classification - Neighbors")
plt.legend(["Test Data", "Training Data"])
plt.savefig("results/graphs/neighbors_{}%{}.png".format(int(acc*100), "accuracy"))

print(classification_report(y_test, y_pred))

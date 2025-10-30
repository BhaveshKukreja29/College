import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

try:
    data = pd.read_csv("college_placement.csv")
except FileNotFoundError:
    print("Error: 'college_placement.csv' not found. Please check the file path.")
    exit()

X = data[['CGPA', 'IQ']]
y = data['Placement']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print(f"The accuracy of the Naive Bayes model is: {acc}")
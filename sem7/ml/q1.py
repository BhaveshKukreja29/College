import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from itertools import combinations
import numpy as np

df = pd.read_csv("Advertising.csv")

df = df.drop(columns=["Unamed: 0"], errors="ignore")

features = ["TV", "Radio", "Newspaper"]
y = df["Sales"]

x_train, x_test, y_train, y_test = train_test_split(
        df[features], y, test_size=0.2, random_state=42
)

results = []

for size in range(1, len(features) + 1):
    for selected in combinations(features, size):

        model = LinearRegression()

        model.fit(x_train[list(selected)], y_train)

        predictions = model.predict(x_test[list(selected)])

        rmse = np.sqrt(mean_squared_error(y_test, predictions))

        r2 = r2_score(y_test, predictions)

        results.append({
            "Features": ", ".join(selected),
            "RMSE": rmse,
            "R2 Score": r2
        })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(
                by="RMSE", ascending=True
            )
print(results_df.to_string(index=False))


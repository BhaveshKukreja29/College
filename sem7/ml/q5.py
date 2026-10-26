import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("Advertising.csv")
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# Features and target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Reserve 20% for testing
X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fractions of the original dataset to use for training
training_sizes = [0.50, 0.70, 0.80]

results = []

for size in training_sizes:

    # Convert original-dataset fraction to fraction of the 80% training pool
    fraction = size / 0.80

    if fraction == 1.0:
        X_train = X_train_full
        y_train = y_train_full
    else:
        X_train, _, y_train, _ = train_test_split(
            X_train_full,
            y_train_full,
            train_size=fraction,
            random_state=42
        )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate on the same test set
    predictions = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    results.append({
        "Training Data (%)": int(size * 100),
        "Training Rows": len(X_train),
        "RMSE": rmse,
        "R2 Score": r2
    })

# Display comparison
results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))

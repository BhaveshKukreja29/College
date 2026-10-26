import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("Advertising.csv")
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# Features and target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict sales
predictions = model.predict(X_test)

# Calculate residuals
residuals = y_test - predictions

# Create results table
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions,
    "Residual": residuals,
    "Absolute_Residual": np.abs(residuals)
})

# Display five largest absolute residuals
print("Five largest prediction errors:")
print(results.nlargest(5, "Absolute_Residual").to_string())

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nRMSE:", rmse)
print("R2 Score:", r2)

# Plot actual versus predicted sales
plt.scatter(y_test, predictions)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")

# Perfect predictions lie on this line
minimum = min(y_test.min(), predictions.min())
maximum = max(y_test.max(), predictions.max())
plt.plot([minimum, maximum], [minimum, maximum], "r--")

plt.tight_layout()
plt.show()

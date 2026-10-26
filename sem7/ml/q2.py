import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from itertools import combinations
import numpy as np

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


df = pd.read_csv("Advertising.csv")

df = df.drop(columns=["Unamed: 0"], errors="ignore")

features = ["TV", "Radio"]
y = df["Sales"]

x_train, x_test, y_train, y_test = train_test_split(
                                        df[features], y, test_size=0.2, random_state=42
                                    )

linear_model = LinearRegression()
linear_model.fit(x_train, y_train)
pred_linear = linear_model.predict(x_test)

rmse_linear = np.sqrt(mean_squared_error(y_test, pred_linear))

r2_linear = r2_score(y_test, pred_linear)

print("Linear")
print("RSME:", rmse_linear, " R^2:", r2_linear)
print()
print()

poly = make_pipeline(
            PolynomialFeatures(degree=4, include_bias=False),
            LinearRegression()
        )

poly.fit(x_train, y_train)
pred_poly = poly.predict(x_test)

rmse_poly = np.sqrt(mean_squared_error(y_test, pred_poly))
r2_poly = r2_score(y_test, pred_poly)


print("Poly")
print("RSME:", rmse_poly, " R^2:", r2_poly)
print()
print()




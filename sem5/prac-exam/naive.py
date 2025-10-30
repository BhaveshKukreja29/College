import pandas as pd
import numpy as np

data = pd.read_csv("college_placement.csv")

train = data.sample(frac=0.8, random_state=1)
test = data.drop(train.index)

priors = train["Placement"].value_counts(normalize=True)
means = train.groupby("Placement").mean()
vars_ = train.groupby("Placement").var()

def prob(x, mean, var):
    if var == 0:
        return 1 if x == mean else 1e-9
    numerator = np.exp(-(x - mean)**2 / (2 * var))
    denominator = np.sqrt(2 * np.pi * var)
    return numerator / denominator

preds = []
for _, row in test.iterrows():
    scores = {}
    for c in priors.index:
        score = np.log(priors[c])
        for col in train.columns[:-1]:
            feature_prob = prob(row[col], means.loc[c, col], vars_.loc[c, col])
            score *= np.log(feature_prob)
        scores[c] = score
    preds.append(max(scores, key=scores.get))

acc = np.mean(np.array(preds) == test["Placement"].values)
print(f"Accuracy: {acc}")
import pandas as pd
import numpy as np

data = pd.read_csv("college_placement.csv")

data = data.drop(columns=["College_ID"])
data["Internship_Experience"] = data["Internship_Experience"].map({"Yes": 1, "No": 0})
data["Placement"] = data["Placement"].map({"Yes": 1, "No": 0})

train = data.sample(frac=0.8, random_state = 1)
test = data.drop(train.index)

priors = train["Placement"].value_counts(normalize=True)

means = train.groupby("Placement").mean()
vars_ = train.groupby("Placement").var()

def prob(x, mean, var):
    return (1/np.sqrt(2*np.pi*var)) * np.exp(-(x-mean)**2 / (2*var))
    
preds = []

for _, row in test.iterrows():
    scores = {}
    for c in priors.index:
        score = priors[c]
        for col in train.columns[:-1]:
            score *= prob(row[col], means.loc[c, col], vars_.loc[c, col])
        scores[c] = score
    preds.append(max(scores, key=scores.get))
    
acc = np.mean(np.array(preds) == test["Placement"].values)

print("Accuracy:", acc)




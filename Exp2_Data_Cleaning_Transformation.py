"""Experiment 2: Data cleaning and transformation before visualization."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw = pd.DataFrame({"Name": ["A", "B", "B", None, "C", "D"],
                    "Score": [70, 80, 80, np.nan, 95, 60],
                    "Age": [18, 19, 19, np.nan, 20, 21]})
clean = raw.drop_duplicates().copy()
clean["Score"] = pd.to_numeric(clean["Score"], errors="coerce")
clean["Score"] = clean["Score"].fillna(clean["Score"].median())
clean["Age"] = clean["Age"].fillna(clean["Age"].median())
clean["Grade"] = pd.cut(clean["Score"], bins=[0, 69, 79, 89, 100],
                        labels=["D", "C", "B", "A"])

print("Cleaned and transformed data:")
print(clean)
clean.plot(kind="bar", x="Name", y="Score", legend=False, title="Scores After Cleaning")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

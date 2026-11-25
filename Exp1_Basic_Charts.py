"""Experiment 1: Basic charts using generated sample data."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
df = pd.DataFrame({"Subject": ["Math", "Physics", "Chemistry", "English", "CS"],
                   "Score": np.random.randint(65, 98, 5)})
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.barplot(data=df, x="Subject", y="Score", ax=axes[0], palette="viridis")
axes[0].set_title("Bar Chart: Scores by Subject")
axes[0].tick_params(axis="x", rotation=20)
axes[1].plot(df["Subject"], df["Score"], marker="o", linewidth=2)
axes[1].set_title("Line Chart: Scores by Subject")
axes[1].set_ylabel("Score")
plt.tight_layout()
plt.show()

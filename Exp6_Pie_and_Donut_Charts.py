"""Experiment 6: Pie and donut charts."""
import pandas as pd
import matplotlib.pyplot as plt

values = pd.Series([35, 25, 20, 15, 5], index=["A", "B", "C", "D", "Other"])
fig, axes = plt.subplots(1, 2, figsize=(11, 5))

axes[0].pie(values, labels=values.index, autopct="%1.1f%%", startangle=90)
axes[0].set_title("Pie Chart")
axes[1].pie(values, labels=values.index, autopct="%1.1f%%", startangle=90,
            wedgeprops={"width": 0.45})
axes[1].text(0, 0, "100%", ha="center", va="center", fontsize=14, weight="bold")
axes[1].set_title("Donut Chart")
plt.tight_layout()
plt.show()

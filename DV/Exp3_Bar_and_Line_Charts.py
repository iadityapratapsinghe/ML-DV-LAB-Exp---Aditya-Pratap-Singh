"""Experiment 3: Combined bar and line charts for monthly sales."""
import pandas as pd
import matplotlib.pyplot as plt

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df = pd.DataFrame({"Month": month,
                   "Sales": [120, 150, 170, 145, 210, 230],
                   "Profit": [30, 45, 52, 40, 70, 78]})

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(df["Month"], df["Sales"], color="lightblue", label="Sales")
ax1.set_ylabel("Sales")
ax2 = ax1.twinx()
ax2.plot(df["Month"], df["Profit"], color="crimson", marker="o", linewidth=2, label="Profit")
ax2.set_ylabel("Profit")
ax1.set_title("Monthly Sales and Profit")
ax1.set_xlabel("Month")
fig.tight_layout()
plt.show()

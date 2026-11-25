"""Experiment 4: Interactive filtering using a Matplotlib dashboard."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

np.random.seed(7)
df = pd.DataFrame({"Day": pd.date_range("2026-01-01", periods=60),
                   "Sales": np.cumsum(np.random.normal(12, 8, 60)) + 200,
                   "Region": np.resize(["North", "South", "East", "West"], 60)})

fig, ax = plt.subplots(figsize=(11, 5))
plt.subplots_adjust(bottom=0.25)
days_slider = Slider(plt.axes([0.15, 0.1, 0.65, 0.03]), "Visible days", 10, 60,
                     valinit=60, valstep=5)

line, = ax.plot(df["Day"], df["Sales"], marker="o", ms=3)
ax.set_title("Interactive Sales Dashboard")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
fig.autofmt_xdate()

def update(value):
    visible = df.tail(int(value))
    line.set_data(visible["Day"], visible["Sales"])
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

days_slider.on_changed(update)
plt.show()

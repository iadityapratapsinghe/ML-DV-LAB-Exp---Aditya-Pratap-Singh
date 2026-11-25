"""Experiment 8: Time-series visualization and moving-average forecasting."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(23)
dates = pd.date_range("2026-01-01", periods=36, freq="ME")
values = 100 + np.arange(36) * 2.5 + np.random.normal(0, 5, 36)
df = pd.DataFrame({"Date": dates, "Demand": values}).set_index("Date")

# Rolling average forecast for the final 6 observed periods.
df["Moving_Average"] = df["Demand"].rolling(window=6, min_periods=1).mean()
future_dates = pd.date_range(df.index[-1] + pd.offsets.MonthEnd(), periods=7, freq="ME")[1:]
forecast = pd.Series([df["Moving_Average"].iloc[-1]] * 6, index=future_dates)

plt.figure(figsize=(11, 5))
plt.plot(df.index, df["Demand"], marker="o", label="Observed")
plt.plot(df.index, df["Moving_Average"], linewidth=2, label="6-Period Moving Average")
plt.plot(forecast.index, forecast.values, "--", marker="o", label="Forecast")
plt.title("Time-Series Demand Forecast")
plt.xlabel("Month")
plt.ylabel("Demand")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

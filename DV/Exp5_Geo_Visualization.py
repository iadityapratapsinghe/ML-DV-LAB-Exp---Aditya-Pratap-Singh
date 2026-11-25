"""Experiment 5: Geographic-style scatter visualization."""
import pandas as pd
import matplotlib.pyplot as plt

cities = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai", "Hyderabad"],
    "Longitude": [77.2090, 72.8777, 77.5946, 88.3639, 80.2707, 78.4867],
    "Latitude": [28.6139, 19.0760, 12.9716, 22.5726, 13.0827, 17.3850],
    "Population_millions": [31.1, 21.0, 13.6, 14.9, 11.0, 10.8]
})

plt.figure(figsize=(9, 6))
scatter = plt.scatter(cities["Longitude"], cities["Latitude"],
                      s=cities["Population_millions"] * 25, c=cities["Population_millions"],
                      cmap="viridis", alpha=0.75, edgecolor="black")
for _, row in cities.iterrows():
    plt.annotate(row["City"], (row["Longitude"] + 0.15, row["Latitude"] + 0.15))
plt.colorbar(scatter, label="Population (millions)")
plt.title("City Population Geo Visualization")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

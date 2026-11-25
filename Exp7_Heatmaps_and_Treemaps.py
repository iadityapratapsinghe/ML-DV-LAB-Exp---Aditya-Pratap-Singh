"""Experiment 7: Heatmap and treemap-style area visualization."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches

np.random.seed(11)
correlation = pd.DataFrame(np.random.rand(5, 5),
                           columns=list("ABCDE"), index=list("ABCDE")).corr()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[0])
axes[0].set_title("Correlation Heatmap")

sizes = {"Python": 40, "Java": 25, "C++": 20, "JavaScript": 15}
colors = plt.cm.Pastel1(np.linspace(0, 1, len(sizes)))
values = list(sizes.values())
labels = list(sizes.keys())
# Simple area split treemap using one horizontal strip per category.
left = 0
for label, value, color in zip(labels, values, colors):
    width = value / sum(values)
    rect = patches.Rectangle((left, 0), width, 1, facecolor=color, edgecolor="white", linewidth=3)
    axes[1].add_patch(rect)
    axes[1].text(left + width / 2, 0.5, f"{label}\n{value}", ha="center", va="center")
    left += width
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1)
axes[1].axis("off")
axes[1].set_title("Treemap-Style Category Area")
plt.tight_layout()
plt.show()

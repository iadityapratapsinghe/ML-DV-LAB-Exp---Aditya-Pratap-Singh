# ML and DV Lab Experiments

A collection of practical Machine Learning and Data Visualization experiments by **Aditya Pratap Singh**.

## Repository Structure

```text
.
├── ML/
│   ├── Exp1_Simple_Linear_Regression.py
│   ├── Exp2_Multiple_Linear_Regression.py
│   ├── Exp3_Logistic_Regression.py
│   ├── Exp4_Regression_with_Regularization.py
│   ├── Exp5_Dimensionality_Reduction_PCA.py
│   ├── Exp6_SVM.py
│   ├── Exp7_Decision_Tree.py
│   ├── Exp8_Naive_Bayes.py
│   └── Exp9_KMeans_Clustering.py
├── DV/
│   ├── Exp1_Basic_Charts.py
│   ├── Exp2_Data_Cleaning_Transformation.py
│   ├── Exp3_Bar_and_Line_Charts.py
│   ├── Exp4_Interactive_Dashboard_Filters.py
│   ├── Exp5_Geo_Visualization.py
│   ├── Exp6_Pie_and_Donut_Charts.py
│   ├── Exp7_Heatmaps_and_Treemaps.py
│   └── Exp8_Time_Series_Forecasting.py
├── requirements.txt
└── README.md
```

## Machine Learning Experiments

| Experiment | Description |
|---|---|
| Exp1 - Simple Linear Regression | Models a target using BMI as a single feature from the diabetes dataset. |
| Exp2 - Multiple Linear Regression | Uses all diabetes features to predict disease progression. |
| Exp3 - Logistic Regression | Performs binary breast-cancer classification with feature scaling. |
| Exp4 - Regularization | Compares Ridge and Lasso regression on the diabetes dataset. |
| Exp5 - PCA | Reduces the digits dataset to two principal components. |
| Exp6 - SVM | Classifies Iris species using a scaled RBF support-vector machine. |
| Exp7 - Decision Tree | Trains a shallow decision-tree classifier on the Iris dataset. |
| Exp8 - Naive Bayes | Applies Gaussian Naive Bayes to wine classification. |
| Exp9 - K-Means | Groups standardized Iris observations into clusters and computes a silhouette score. |

## Data Visualization Experiments

| Experiment | Description |
|---|---|
| Exp1 - Basic Charts | Creates basic bar and line charts from sample subject scores. |
| Exp2 - Data Cleaning | Demonstrates duplicate removal, missing-value handling, and categorical transformation. |
| Exp3 - Bar and Line Charts | Displays monthly sales and profit together with dual axes. |
| Exp4 - Interactive Dashboard | Builds a slider-controlled sales time-series dashboard. |
| Exp5 - Geo Visualization | Plots Indian city locations using coordinates and population bubbles. |
| Exp6 - Pie and Donut Charts | Compares category proportions in pie and donut layouts. |
| Exp7 - Heatmaps and Treemaps | Demonstrates correlation heatmaps and an area-based treemap-style view. |
| Exp8 - Time-Series Forecasting | Visualizes observed demand and a moving-average forecast. |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run any experiment from the repository root:

```bash
python ML/Exp1_Simple_Linear_Regression.py
python DV/Exp1_Basic_Charts.py
```

# PRODIGY_ML_02
# Customer Segmentation Using K-Means Clustering

## Overview
This project focuses on segmenting customers using K-Means clustering based on their annual income, spending scores, and age. The dataset used for analysis is `Mall_Customers.csv`, which contains various attributes of customers visiting a mall.

## Code Summary
- **Libraries Used**: 
  - `numpy`: For numerical operations.
  - `pandas`: For data manipulation.
  - `matplotlib.pyplot`: For visualization.
  - `sklearn.cluster`: For implementing K-Means clustering.

- **Dataset**: 
  - The `Mall_Customers.csv` file is loaded into a DataFrame to extract features relevant for clustering.

- **Elbow Method**: 
  - The optimal number of clusters is determined using the elbow method, which evaluates the Within-Cluster Sum of Squares (WCSS) for different cluster numbers.

- **Clustering**: 
  - K-Means clustering is applied to segment customers based on:
    1. **Annual Income and Spending Score**: Results are visualized in a scatter plot showing customer distribution across clusters.
    2. **Age and Annual Income**: A second clustering method is applied, and results are visualized similarly.

## Conclusion
This project demonstrates the application of K-Means clustering for effective customer segmentation. The visualizations provide insights into customer behavior, which can be beneficial for targeted marketing strategies.

# PRODIGY_ML_02
# Customer Segmentation Using K-Means Clustering

## Overview
This project focuses on segmenting customers using K-Means clustering based on their annual income and spending scores, as well as their age and annual income. The dataset used for analysis is `Mall_Customers.csv`, which contains various attributes of customers visiting a mall.

### 1. Importing Libraries
The code begins by importing the necessary libraries:
- `numpy`: For numerical operations and handling arrays.
- `pandas`: For data manipulation and analysis, particularly for working with tabular data.
- `matplotlib.pyplot`: For visualizing results through plots.
- `sklearn.cluster`: Specifically, `KMeans` for implementing the K-Means clustering algorithm.

### 2. Loading the Dataset
The dataset is loaded using `pandas`:
- The `Mall_Customers.csv` file is read into a DataFrame, `df`.
- The features used for clustering, specifically annual income and spending score, are extracted into the variable `X`.

### 3. Finding the Optimal Number of Clusters Using the Elbow Method
The elbow method is employed to determine the optimal number of clusters:
- A loop runs from 1 to 10 to fit K-Means models with different numbers of clusters.
- The Within-Cluster Sum of Squares (WCSS) is calculated for each model and stored in the `wcss` list.
- A plot is generated to visualize the WCSS against the number of clusters, allowing for identification of the "elbow" point, which indicates the optimal number of clusters.

### 4. First Clustering Method: Annual Income and Spending Score
K-Means clustering is applied to segment customers based on their annual income and spending score:
- The K-Means model is trained with 5 clusters.
- The model predicts cluster labels for each customer, stored in `y_kmeans`.

### 5. Visualizing the Clusters for Annual Income and Spending Score
A scatter plot is created to visualize the clusters:
- Each cluster is represented by a different color, with the customers’ annual income on the x-axis and their spending score on the y-axis.
- The cluster centroids are highlighted in yellow.

### 6. Second Clustering Method: Age and Annual Income
Another clustering approach is conducted using age and annual income:
- The relevant features (age and annual income) are extracted into the variable `Z`.
- The K-Means model is again trained with 5 clusters, and predictions are made.

### 7. Visualizing the Clusters for Age and Annual Income
A scatter plot is generated to visualize the customer segments:
- Each cluster is depicted in different colors, with age on the x-axis and annual income on the y-axis.
- The centroids of the clusters are also highlighted in yellow.

## Conclusion
This project demonstrates the application of K-Means clustering for customer segmentation based on key attributes. The visualizations provide insights into the distribution of customers across different clusters, which can be useful for targeted marketing strategies and understanding customer behavior.

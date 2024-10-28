# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Importing the dataset
df = pd.read_csv('Mall_Customers.csv')
X = df.iloc[:, [3,4]].values

# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('The Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# First Clustering Method between Annual Income (k$) & Spending Score (1-100)
# Training the K-Means model on the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(X)

# Visualizing the Clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'magenta', label = 'Cluster 1') 
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'cyan', label = 'Cluster 2') 
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3') 
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'blue', label = 'Cluster 4') 
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'red', label = 'Cluster 5') 
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# Second Clustering Method between Age & Annual Income (k$) 
Z = df.iloc[:, [2,3]].values

# Training the K-Means model on the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 0)
clusters = kmeans.fit_predict(Z)

# Visualizing the Clusters
plt.scatter(Z[clusters == 0, 0], Z[clusters == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(Z[clusters == 1, 0], Z[clusters == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(Z[clusters == 2, 0], Z[clusters == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(Z[clusters == 3, 0], Z[clusters == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(Z[clusters == 4, 0], Z[clusters == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Age')
plt.ylabel('Annual Income (k$)')
plt.legend()
plt.show()


import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans

# Load the data from the CSV file
data = pd.read_csv('./data/consumption.csv')

# Weight latitude and longitude
GEO_WEIGHT = .1 # Higher value prioritizes geographic proximity over taste similarity

# Weight Latitude and Longitude
data['Latitude'] *= GEO_WEIGHT
data['Longitude'] *= GEO_WEIGHT

# Perform K-means clustering on districts by past consumption and geography
kmeans = KMeans(n_clusters=6,n_init=30)
y = kmeans.fit_predict(data.drop(columns=['District', 'Median Income']))
data['Cluster'] = y

# Write clusters to new csv file
data.to_csv('consumption_with_clusters.csv', index=False)

plt.figure(figsize=(6, 12))
plt.scatter(data['Latitude']/GEO_WEIGHT, data['Longitude']/GEO_WEIGHT,c=data['Cluster'], cmap="Dark2")
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

plt.title(f"KMeans Clusters, Geographic Weight: {GEO_WEIGHT}",size=18)
plt.xlabel("Longitude",size=14)
plt.ylabel("Latitude",size=14)
plt.axis("equal")
plt.savefig('plot.png')

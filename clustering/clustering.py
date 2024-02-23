import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans

# Load consumption data
data = pd.read_csv('../data/consumption.csv')

# Weight latitude and longitude
GEO_WEIGHT = .0001 # Higher value prioritizes geographic proximity over taste similarity
data[['Latitude', 'Longitude']] *= GEO_WEIGHT

# Perform K-means clustering on districts by past consumption and geography
kmeans = KMeans(n_clusters=6,n_init=30)
y = kmeans.fit_predict(data.drop(columns=['District', 'Median Income']))
data['Cluster'] = y

# Save cluster assignments
data[['District', 'Cluster']].to_csv('clusters.csv', index=False)

#########################
# Convert cluster consumption into preferences
#########################

# Split dataframe by crop type (pulse or grain)
grains = ['jowar','bajra','barley','maize','small millets','ragi']
pulses = ['arhar','moong','masur','urd','peas','khesari','gram products','besan']
data_pulses = data.drop(columns=grains+['Median Income', 'Latitude', 'Longitude'])
data_grains = data.drop(columns=pulses+['Median Income', 'Latitude', 'Longitude'])

# Group by cluster and calculate median for each food item
pulses_summary = data_pulses.groupby('Cluster').median()
grains_summary = data_grains.groupby('Cluster').median()

# Convert cluster medians to preferences with softmax
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

pulses_softmax = pulses_summary.apply(softmax, axis=1)
grains_softmax = grains_summary.apply(softmax, axis=1)

# Combine pulse and grain dataframes and save to csv 
combined = pd.concat([grains_softmax, pulses_softmax], axis=1)
combined.to_csv("cluster_preferences.csv")

# Create cluster map plot
plt.figure(figsize=(6, 12))
plt.scatter(data['Latitude']/GEO_WEIGHT, data['Longitude']/GEO_WEIGHT,c=data['Cluster'], cmap="Dark2")
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.title(f"KMeans Clusters, Geographic Weight: {GEO_WEIGHT}",size=18)
plt.xlabel("Longitude",size=14)
plt.ylabel("Latitude",size=14)
plt.axis("equal")
plt.savefig('cluster_map.png')

# Create crop preferences plot
combined.plot(kind='bar', figsize=(20,10))
plt.title('Relative crop preferences by cluster')
plt.ylabel('Preference')
plt.xlabel('Cluster')
plt.savefig('preferences.png')
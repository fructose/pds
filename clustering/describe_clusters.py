import pandas as pd
import matplotlib.pyplot as plt

grains = ['jowar','bajra','barley','maize','small millets','ragi']
pulses = ['arhar','moong','masur','urd','peas','khesari','gram products','besan']


data = pd.read_csv("consumption_with_clusters.csv").drop(columns=['Median Income', 'Latitude', 'Longitude'])
print(data.columns)

data_pulses = data.drop(columns=grains)
data_grains = data.drop(columns=pulses)

# Group by Cluster and calculate median for each food item
median_df = data.groupby('Cluster').median()

print(median_df.head(1))

# rank the median consumption in each cluster and then reverse the rank
ranked_df = median_df.rank(ascending=False).astype(int)

print(ranked_df.head(1))

# Plotting mean consumption for each cluster
median_df.plot(kind='bar', figsize=(20,10))
plt.title('Mean Consumption for Each Cluster')
plt.ylabel('Mean Consumption')
plt.xlabel('Cluster')
plt.show()
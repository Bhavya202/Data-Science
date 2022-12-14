# Importing Modules
import csv
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Reading The CSV
rows = []
with open("main.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

# Reading The Headers And The Rows
headers = rows[0]
planet_data_rows = rows[1:]

# Extracting Planet Mass, Planet Radius And Planet Names
planet_mass = []
planet_radius = []
planet_name = []
for planet_data in planet_data_rows:
    planet_mass.append(planet_data[3])
    planet_radius.append(planet_data[4])
    planet_name.append(planet_data[1])

# Claculating The Gravity Of All Planets
planet_gravity = []
for index, name in enumerate(planet_name):
    gravity = (float(planet_mass[index])*1.989e+30) / (float(planet_radius[index])*float(planet_radius[index])*6.957e+8*6.957e+8) * 6.674e-11
    planet_gravity.append(gravity)

# Plotting A Bar Graph With Planet Names And Their Gravity
fig = px.scatter(x=planet_name, y=planet_gravity)
fig.layout.update({
    "title": "Planets With Their Gravity",
    "xaxis": {"title": "Planet Names"},
    "yaxis": {"title": "Planet Gravity"},
})
fig.show()

# Creating Charts
# Charts Of Mass And Radius Of The Planets With Respect To Gravity
fig = px.scatter(x=planet_mass, y=planet_radius, color=planet_gravity, hover_name=planet_name)
fig.layout.update(
    coloraxis_colorbar=dict(
        title="Gravity",
    )
)
fig.layout.update({
    "title": "Mass And Radius Of The Planets With Respect To Gravity",
    "xaxis": {"title": "Mass"},
    "yaxis": {"title": "Radius"},
})
fig.show()

# Charts Of Mass And Gravity Of The Planets With Respect To Radius
fig = px.scatter(x=planet_mass, y=planet_gravity, color=planet_radius, hover_name=planet_name)
fig.layout.update(
    coloraxis_colorbar=dict(
        title="Radius",
    )
)
fig.layout.update({
    "title": "Mass And Gravity Of The Planets With Respect To Radius",
    "xaxis": {"title": "Mass"},
    "yaxis": {"title": "Gravity"},
})
fig.show()

# Finding The Number Of Clusters
X = []
for index, planet_mass in enumerate(planet_mass):
  temp_list = [
                  planet_radius[index],
                  planet_mass
              ]
  X.append(temp_list)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)
    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Taking Out The Distance From The Data
distance = []
for planet_data in planet_data_rows:
    distance.append(planet_data[2])

# Rounding Off The Data As It Has Decimal Values
round = [int(round(float(i))) for i in distance]

# Making A New List Of Distance
new_distance = []
for data in round:
    if data <= 100:
        new_distance.append(data)

# Making A New List of Planet Gravity
new_gravity = list(planet_gravity)
for planet_data in planet_gravity:
  if planet_data > 350 or planet_data < 50:
    new_gravity.remove(planet_data)

# Printing Number Of New Planet Distanc And Gravity
print(len(new_distance))
print(len(new_gravity))

# Creating A New CSV File
df2 = pd.DataFrame(list(zip(planet_name, distance, planet_mass, planet_radius, planet_gravity)), columns=['Name','Distance','Mass','Radius', 'Gravity'])
df2.to_csv('data.csv')
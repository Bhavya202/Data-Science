# Importing Modules
import csv
import plotly.express as px

# Reading The CSV
rows = []
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

# Reading The Headers And The Rows
headers = rows[0]
planet_data_rows = rows[1:]

# Extracting Planet Mass, Planet Radius And Planet Names
planet_name = []
planet_distance = []
planet_mass = []
planet_radius = []
planet_gravity = []
for planet_data in planet_data_rows:
    planet_name.append(planet_data[1])
    planet_distance.append(planet_data[2])
    planet_mass.append(planet_data[3])
    planet_radius.append(planet_data[4])
    planet_gravity.append(planet_data[5])

# Plotting The Charts
# Planet Name VS Distance Graph
fig = px.scatter(x=planet_name, y=planet_distance)
fig.layout.update({
    "title": "Planet Names And Their Distance From Light Years",
    "xaxis": {"title": "Planet Names"},
    "yaxis": {"title": "Distance"}
})
fig.show()
# This Chart Shows That They Are Not In A Linear Regression
# The Data Is Scatterd
# So The Dots On The Chart Is Evenly Scattered

# Planet Name VS Mass Graph
fig = px.scatter(x=planet_name, y=planet_mass)
fig.layout.update({
    "title": "Planet Names And Their Mass",
    "xaxis": {"title": "Planet Names"},
    "yaxis": {"title": "Mass"}
})
fig.show()
# The graph is not evenly scattered in the starting
# But as it goes towards the end it starts scaterring 
# We can notice some small building like structure and overlapping of planets mass in each other

# Planet Name VS Radius Graph
fig = px.scatter(x=planet_name, y=planet_radius)
fig.layout.update({
    "title": "Planet Names And Their Radius",
    "xaxis": {"title": "Planet Names"},
    "yaxis": {"title": "Radius"}
})
fig.show()
# The graph is same like previos one
# Scattering at the last
# It represents the path of going up the hill and as we are going up the surface is going rough
# It means that scattering of data is more at end

# Planet Name VS Gravity Graph
fig = px.scatter(x=planet_name, y=planet_gravity)
fig.layout.update({
    "title": "Planet Names And Their Gravity",
    "xaxis": {"title": "Planet Names"},
    "yaxis": {"title": "Gravity"}
})
fig.show()
# This graph is same like previous one
# It follows a linear regression at the starting
# It seems like we are climbing a mountain has has a straight path
# The path seems to be going up and be rough at the peak
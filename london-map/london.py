import folium
import pandas

# get the data
stations = pandas.read_csv("london-underground-stations.txt")
lat = list(stations["y"])
lon = list(stations["x"])
name = list(stations["NAME"])

# create the map with starting view
map_london = folium.Map(location=[51.52802450525226, -0.12495022217516479], zoom_start=10)

# add features to the map
fg = folium.FeatureGroup(name="London Underground Stations")
for lat, lon, name in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color='blue')))
    map_london.add_child(fg)


map_london.save("london.html")

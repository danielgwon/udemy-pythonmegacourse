import folium
import pandas

# get the data
stations = pandas.read_csv("london-underground-stations.txt")
lat = list(stations["y"])
lon = list(stations["x"])
name = list(stations["NAME"])
lines = list(stations["LINES"])

# customize the popup
popup_html = "<strong>Name</strong>: %s<br><strong>Lines</strong>: %s"

def distanceColor(lat, lon):
    return 'green'

"""
def coordinatesToDistance
"""

# create the map with starting view
map_london = folium.Map(location=[51.52802450525226, -0.12495022217516479], zoom_start=10)

# add features to the map
fg = folium.FeatureGroup(name="London Underground Stations")
for lat, lon, name, lines in zip(lat, lon, name, lines):

    # insert custom popup HTML
    iframe = folium.IFrame(html=popup_html % (name, lines), width=200, height=75)

    fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color=distanceColor())))
map_london.add_child(fg)


map_london.save("london.html")

import folium
import pandas

# get the data
volcanoes = pandas.read_csv("volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
name = list(volcanoes["NAME"])
elev = list(volcanoes["ELEV"])

# create the map with starting view
us_volcanoes = folium.Map(location=[40.59187878635517, -111.7541061476434], zoom_start=5, tiles="Stamen Terrain")

# dynamically determine popup color based on elevation
def getElevationColor(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation < 2500:
        return 'orange'
    else:
        return 'red'

# customize the popup
popup_html = "<strong>Name</strong>: %s<br><strong>Elevation</strong>: %sm"

# add features to the map
fg = folium.FeatureGroup(name="Volcanoes")
for lat, lon, name, elev in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=popup_html % (name, elev), width=200, height=75)    # insert custom popup HTML
    fg.add_child(folium.CircleMarker((lat, lon), radius=6, popup=folium.Popup(iframe), color='grey',
    fill_color=getElevationColor(elev), fill=True, fill_opacity=0.7))
us_volcanoes.add_child(fg)


us_volcanoes.save("volcanoes.html")

#TODO unable to click volcano popup when population layer is active

import folium
import pandas

# create the map with starting view
volcanoPopulationMap = folium.Map(location=[40.41492280892401, 21.678399183565926], zoom_start=2, tiles="Stamen Terrain")

# get volcano data
volcanoes = pandas.read_csv("volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
name = list(volcanoes["NAME"])
elev = list(volcanoes["ELEV"])

# get population data
worldDataFile = open("world.json", 'r', encoding='utf-8-sig')
worldData = worldDataFile.read()
worldDataFile.close()

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

# add volcano features to the map
fgv = folium.FeatureGroup(name="Volcanoes")
for lat, lon, name, elev in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=popup_html % (name, elev), width=200, height=75)    # insert custom popup HTML
    fgv.add_child(folium.CircleMarker((lat, lon), radius=6, popup=folium.Popup(iframe), color='grey',
    fill_color=getElevationColor(elev), fill=True, fill_opacity=0.7))

# add polygon layer with colors based on population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=worldData,
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'yellow' if 10000000 <= x['properties']['POP2005'] < 50000000
else 'orange' if 50000000 <= x['properties']['POP2005'] < 100000000
else 'red'}))

volcanoPopulationMap.add_child(fgv)
volcanoPopulationMap.add_child(fgp)
volcanoPopulationMap.add_child(folium.LayerControl())
volcanoPopulationMap.save("volcanoPopulationMap.html")

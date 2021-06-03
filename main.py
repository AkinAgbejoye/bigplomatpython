import  folium
import pandas
map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My name")
volcanoes =  pandas.read_csv("4.1 Volcanoes.txt")
def colorProducer(elevation):
    if elevation <1000:
        return  "green"
    elif 1000 <= elevation <3000:
        return "blue"
    else:
        return "red"

lat =  list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])
for x, y, el in zip(lat,lon, elev):
    fg.add_child(folium.Marker(location=[x,y],radius=0.7,fill_color=colorProducer(el),color="grey",fill_opacity=0.7,popup=str(el)+"m",icon=folium.Icon(color=colorProducer(el))))
    print(x,y)
map.add_child(fg)

map.save("cotonou.html")
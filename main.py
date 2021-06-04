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
    fg.add_child(folium.CircleMarker(location=[x,y],radius=6,fill_color=colorProducer(el),color="grey",fill_opacity=0.7,popup=str(el)+"m"))
    #print(x,y)


fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
map.add_child(fg)

map.save("cotonou.html")
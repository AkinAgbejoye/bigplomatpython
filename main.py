import  folium

map = folium.Map(location=[6.372297886155456, 2.3872484608488485],zoom_start=6,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My name")
fg.add_child(folium.Marker(location=[6.372297886155456, 2.3872484608488485],popup="Hi There",icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("cotonou.html")
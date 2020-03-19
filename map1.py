import folium
import pandas

#Data of airports
data_air = pandas.read_csv("airport_india.txt")
lat_air = list(data_air["latitude_deg"])
lon_air = list(data_air["longitude_deg"])
gps = list(data_air["gps_code"])


#Data for city population
data_popu = pandas.read_csv("india_popu.csv")
lat_popu = list(data_popu["lat"])
lon_popu = list(data_popu["lng"])
popu = list(data_popu["population"])
city = list(data_popu["city"])

#Global variable
tool = "Click for more information"



map = folium.Map(location = [20.5937 ,78.9629], zoom_start=4)

fg_air = folium.FeatureGroup(name="Airport")

for lt, ln, code in zip(lat_air, lon_air, gps):
    fg_air.add_child(folium.Marker(location=[lt, ln],
                               radius = 5,
                               popup=code,
                               icon=folium.features.CustomIcon("flight_icon.png", icon_size=(50,50)),
                               tooltip = tool,
                               ))


fg_pop = folium.FeatureGroup(name = "Indian City population")

for lt, ln, pol, city in zip(lat_popu, lon_popu, popu, city):
    fg_pop.add_child(folium.Marker(location=[lt, ln],
                               tooltip = tool,
                               popup = city + "\n Population: " + str(pol)
                               ))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data =(open('world.json', 'r', encoding = 'utf-8-sig').read()),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'orange' if x['properties']['POP2005'] < 2000000 else 'red'}))



map.add_child(fg_air)
map.add_child(fg_pop)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

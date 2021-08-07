import folium 
import pandas 

data = pandas.read_excel("lowkayshin.xlsx", sheet_name=0)

name_of_city = list(data["location"])
lon = list(data["Longitude"])
lat = list(data["Latitude"])
mnpop = list(data["Population"])

def color_producer(mnpopulation):
    if mnpopulation < 1000:
        return 'grey'
    elif 1000 <= mnpopulation < 10000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[44.937, -93.0900], zoom_start=8.5, tiles="Stamen Terrain")

fg_unemployment = folium.FeatureGroup(name="Unemployment")

for lt, ln, pops, name in zip(lat, lon, mnpop, name_of_city):
    fg_unemployment.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=" {} \nPopulation = {}".format(name, pops), 
    fill_color=color_producer(pops), color = 'grey', fill_opacity=0.7))



map.add_child(fg_unemployment)

map.save("soda1.html")
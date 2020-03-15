import folium
import pandas as pd
import math

# create main map
m = folium.Map(location=[55.741467, -4.513410], zoom_start=6)

#create point
marker = folium.Marker(location=[55.741467, -4.513410],
                       popup="Middle of the map",
                       tooltip="Middle",
                       icon=folium.Icon(icon="fa-heart-o", prefix="fa", color="red"))
m.add_child(marker)

data_frame = pd.read_csv('D:\\Google Drive\\Python\\Collision_data\\Acc_2018.csv', dtype=object)

for row in data_frame.itertuples():
    lat = row.Latitude
    long = row.Longitude
    print(lat, long)
    if isBlank(lat):
        continue
    desc = f'Date: {row.Date}\n' \
           f'Time: {row.Time}'
    ref = row.Accident_Index
    severity_colour = "blue"
    collision = folium.Marker(location=[lat, long],
                              popup=desc,
                              tooltip=ref,
                              icon=folium.Icon(icon="fa-heart-o", prefix="fa", color=severity_colour))
    m.add_child(collision)


# save map
m.save('map.html')
print("hdsajh")


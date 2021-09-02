from urllib.request import urlopen
import json
from geojson import Feature, FeatureCollection, Point

URL = "https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Fire_Points/Text/2021/09/hms20210902.txt"
data = urlopen(URL)
event_list = []
features = []

def clean_data(line):
    decode = line.decode("utf-8")
    
    event = []
    for item in decode.split(","):
        item = item.strip()
        event.append(item)
    return event

def to_geojson(event_list):
    events_json = []
    for event in event_list:
        latitude, longitude = map(float, (event[1],event[0]))
        events_json.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'YearDay': event[2],
                    'Time': event[3],
                    'Satellite': event[4],
                    'Method of Detect': event[5],
                    'Ecosys': event[6],
                    'Fire RadPower': event[7]
                }
            )
        )
    return events_json

# process data to lists
for line in data:
    event_list.append(clean_data(line))

# remove header    
event_list.pop(0)
features = to_geojson(event_list)
collection = FeatureCollection(features)

# write to file 
with open("fires.json", "w") as f:
    f.write('%s' % collection)


    
print(event_list)
    
from urllib.request import urlopen
from datetime import date
import json, sys, getopt
from geojson import Feature, FeatureCollection, Point


event_list = []
features = []
today = date.today()

def get_data(date):
    baseURL = "https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Fire_Points/Text/" 
    if date == "":
        file_path = today.strftime("%Y")+"/"+today.strftime("%m")+"/"+"hms"+today.strftime("%Y%m%d")+".txt"
    else:
        file_path = date[0:4]+"/"+date[4:6]+"/hms"+date+".txt"
    
    URL = baseURL+file_path
    print(URL)
    return urlopen(URL)

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

if len(sys.argv) > 1:
    data = get_data(sys.argv[1])
else:
    data = get_data("")

for line in data:
    event_list.append(clean_data(line))

# remove header    
event_list.pop(0)
features = to_geojson(event_list)
collection = FeatureCollection(features)

# write to file 
if len(sys.argv) > 1:
    file_out = "fires_"+sys.argv[1]+".json"
else:
    file_out = "fires_"+today.strftime("%Y%m%d")+".json"
with open(file_out, "w") as f:
    f.write('%s' % collection)
    
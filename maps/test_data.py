from pykafka  import KafkaClient, client
from pykafka.common import Message 
import json 
from datetime import datetime 
import uuid


input_file = open('./json_data.json')
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']
#print(cordinates)



## generate uuid 

def generate_uuid():
    return uuid.uuid4()

data = {}

data['busline'] = '00001'



## construct messages 

def generate_checkpoint(coordinates):
    i = 0 
    while i < len(coordinates):
        data['key'] = data['busline']+ "__" + str(generate_uuid)
        data['timestamp']= str(datetime.utcnow())
        data['latitude'] = coordinates[0][1]
        data['longitude'] = coordinates[0][0]
        print("message")
        i = i + 1
        print(data)



generate_checkpoint(coordinates)

## sending to the kafka 

from pykafka  import KafkaClient, client
from pykafka.common import Message 
import json 


client = KafkaClient(hosts='Localhost:9092')

topic = client.topics['testBusdata']

producer = topic.get_sync_producer()

count = 1 

while True:
    message = ("hello" + str(count)).encode("ascii")
    producer.produce(message)
    print(message)
    count = count+1 
    if(count == 5000):
        break


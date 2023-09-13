# %%
# Install required libraries
# !pip install avro-python3 confluent-kafka


# %%
# Import required libraries
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer 
from time import sleep
import json
import csv


# %%
# Function to load avro schema file 
def load_avro_schemafile(key_schemafile:str,value_schemafile:str):
    key_schema = avro.load(key_schemafile)
    value_schema = avro.load(value_schemafile)
    return key_schema, value_schema

    

# %%
# Setup config
config = {
    'bootstrap.servers' : 'localhost:9092',
    'schema.registry.url' :'http://0.0.0.0:8081',
    'acks' : "1"

}

# %%
# Extract key schema and value schema
key_schema,val_schema = load_avro_schemafile('taxi_ride_key.avsc','taxi_ride_value.avsc')

# %%
# Instantiate producer
producer = AvroProducer(config,default_key_schema=key_schema,default_value_schema=val_schema)

# %%
# Open csv file and skip the header
f = open('rides.csv','r')
csv_f = csv.reader(f)
next(csv_f)

# %%
# Iterate each row and produce to message broker
for row in csv_f:
    key = {"vendorId":int(row[0])}
    val = {
        "vendorId"  : int(row[0]),
        "passenger_count": int(row[3]),
        "trip_distance":float(row[4]),
        "payment_type": int(row[9]),
        "total_amount": float(row[-2])
        }
    try:
        producer.produce(topic= 'digitalskola.taxi.rides',key=key,value=val)
    except Exception as e:
        print(f"Exception while produding records - {val} {e}")
    else:
        print(f'succesfully producing records - {val}')
    producer.flush()
    sleep(3)
    



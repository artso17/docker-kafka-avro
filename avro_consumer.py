# Import required libraries
from confluent_kafka.avro import AvroConsumer
from time import sleep

# Setup avro consumer config
config = {
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081',
    'group.id' : 'digitalskola.consumer',
    'auto.offset.reset': 'earliest'
}

# Instantiate avro consumer
consumer = AvroConsumer(config)
consumer.subscribe(['digitalskola.taxi.rides'])

# Run consumer
while True:
    try:
        messages = consumer.poll(1)
    except Exception as e:
        print(f'Exeption while pulling messages - {e}')
    else:
        if messages :
            print(f"""Successfully pulling messages \n\t Kafka Topic : {messages.topic()}, Partition : {messages.partition()}, Offset : {messages.offset()} \n\t Message key : {messages.key()}, Value : {messages.value()}
                   """
                   )
            consumer.commit()
        else:
            print('No new message at this point, try again ...')
    sleep(5)
consumer.close()

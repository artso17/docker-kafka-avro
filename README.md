# Data Streaming Simulation Using Apache Kafka and Docker 

## Project Brief
The Project aimed to gain and prove my skills in Data Engineering that is streaming processing using Apache Kafka as message broker and streaming tool which run on Docker using docker-compose. In this case, rides.csv is the data source.

## Success Criteria
1. Install kafka broker using docker compose
1. Create avro schema
2. install avro-python3, confluent-kafka
3. Create kafka producer using python package (use avro schema)
4. Create kafka consumer using python package that consume a topic

## Result
- All Kafa features are setup in `docker-compose.yml`
- All avro schema in `taxi_ride_key.avsc` and `taxi_ride_value.avsc`
- Installed avro-python3 and confluent-kafka in virtual environment
- Created kafka producer namely `avro_producer.py` and used avro schema
- Created kafka consumer that consumed topic `digitalskola.taxi.rides` namely `avro_consumer.py`


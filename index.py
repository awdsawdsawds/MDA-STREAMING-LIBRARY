# import msgpack
from kafka import KafkaConsumer

consumer = KafkaConsumer(
  bootstrap_servers="52.77.249.163:9092",
  # value_deserializer=msgpack.loads,
)

consumer.subscribe(['information'])

for msg in consumer:
  print("===============")
  print(msg.value)
  print(msg.value.decode('utf-8'))
  print("===============")
  # assert isinstance(msg.value, dict)

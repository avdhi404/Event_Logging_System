from confluent_kafka import Producer
import time

def delivery_report(err, msg):
    """Callback function to confirm message delivery."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_events():
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    for i in range(1, 11):  # Simulate 10 events
        event = f"Event {i}"
        producer.produce('event_logging', value=event, callback=delivery_report)
        print(f"Produced: {event}")
        producer.flush()  # Ensure all messages are sent
        time.sleep(1)  # Simulate real-time event logging

if __name__ == '__main__':
    produce_events()

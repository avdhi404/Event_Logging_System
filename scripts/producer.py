from confluent_kafka import Producer
import time
import requests

def delivery_report(err, msg):
    """Callback function to confirm message delivery."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def fetch_data_from_api():
    """Fetch real-time data from an API."""
    url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the fetched JSON data
    else:
        return []

def produce_events():
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    while True:
        data = fetch_data_from_api()  # Fetch data from an API in real-time
        for item in data:
            event = f"Event {item['id']}: {item['title']}"  # Example event data
            producer.produce('event_logging', value=event, callback=delivery_report)
            print(f"Produced: {event}")
            producer.flush()
        time.sleep(5)  # Sleep for 5 seconds before fetching new data

if __name__ == '__main__':
    produce_events()

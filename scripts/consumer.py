from confluent_kafka import Consumer
import sqlite3

def setup_database():
    """Initialize SQLite database to store events."""
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

def consume_events():
    """Consume messages from Kafka and log them into SQLite."""
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'event_group',
        'auto.offset.reset': 'earliest'  # Start from the earliest message
    })
    consumer.subscribe(['event_logging'])

    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()

    print("Consumer is running. Press Ctrl+C to exit.")

    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for new messages with a 1-second timeout
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            event = msg.value().decode('utf-8')
            print(f"Consumed: {event}")
            cursor.execute('INSERT INTO events (message) VALUES (?)', (event,))
            conn.commit()
    except KeyboardInterrupt:
        print("Exiting consumer...")
    finally:
        conn.close()
        consumer.close()

if __name__ == '__main__':
    setup_database()
    consume_events()

# Kafka-based Event Logging System

This project implements an event logging system using Apache Kafka for real-time event processing. The system consists of two main components: the producer and the consumer. The producer generates events and sends them to a Kafka topic, while the consumer listens for events and processes them in real-time.

## Project Structure

```
kafka_event/
│
├── producer.py         # Producer script for generating and sending events to Kafka
├── consumer.py         # Consumer script for consuming and processing events from Kafka
├── kafka/libs/         # Contains libraries and dependencies
│
└── .gitignore          # Files to be ignored by Git (e.g., large files, dependencies)
```

## Prerequisites

Before running the project, make sure you have the following installed:

- **Apache Kafka**: This project uses Kafka as the event streaming platform.
- **Zookeeper**: Kafka relies on Zookeeper for coordination.
- **Python**: The event producer and consumer are implemented in Python.

### Install Kafka and Zookeeper

1. Download the Kafka binary from [Apache Kafka Downloads](https://kafka.apache.org/downloads).
2. Extract the downloaded `.tgz` file and navigate to the `kafka` folder.
3. Start Zookeeper:
   ```
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```
4. Start Kafka server:
   ```
   bin/kafka-server-start.sh config/server.properties
   ```

### Install Python

1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. Install the required Python libraries:
   ```
   pip install kafka-python
   pip install sqlite3
   pip install requests
   ```

## Running the Project

### 1. Producer: `producer.py`

The producer script generates and sends events to a Kafka topic. To run the producer:

1. Ensure Kafka and Zookeeper are running.
2. Run the `producer.py` script:
   ```
   python producer.py
   ```

This will produce 10 events and send them to the Kafka topic `event_logging` every second.

### 2. Consumer: `consumer.py`

The consumer script listens for events from the Kafka topic and processes them. To run the consumer:

1. Ensure Kafka and Zookeeper are running.
2. Run the `consumer.py` script:
   ```
   python consumer.py
   ```

This will consume events from the `event_logging` Kafka topic and print them to the console. You can modify the script to store events in a database or take other actions.

## .gitignore

The `.gitignore` file ensures that unnecessary files, such as large binaries and dependencies, are not tracked in the Git repository. Add the following lines to the `.gitignore` file:

```
# Ignore large files
*.tgz
*.jar

# Ignore Python cache files
__pycache__/
*.pyc

# Ignore Kafka logs
/logs
```

## Troubleshooting

- Ensure Kafka and Zookeeper are properly running before starting the producer and consumer scripts.
- If you encounter any issues with large file sizes, consider using [Git Large File Storage (LFS)](https://git-lfs.github.com) for storing large files in your repository.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

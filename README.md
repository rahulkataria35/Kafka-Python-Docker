# Kafka-Python-Docker

> The major goal of this project was to learn how to use the Kafka, Python, and Docker tools to develop an application that uses the fake database to transmit and receive data (Produce and Consume), as well as to put data into the database.


> Let's start with What is Kafka :

Kafka is a distributed message streaming platform that uses publish and subscribe mechanism to stream the records.

# The role of Kafka in a microservices architecture.

Kafka plays a crucial role in a microservices architecture as it provides a scalable and fault-tolerant messaging system that enables communication between different services. It serves as a distributed streaming platform, allowing the exchange of real-time data streams and event-driven communication among microservices.

# Here are the main roles of Kafka in a microservices architecture:

1. **Event Sourcing and CQRS**: Kafka acts as a log-based message queue where microservices can publish events and other services can consume those events. This facilitates implementing Event Sourcing, a pattern that stores all changes as a sequence of events. It also supports Command Query Responsibility Segregation (CQRS), where commands and queries are separated, enhancing scalability and flexibility.

2. **Decoupling and Asynchronous Communication**: Kafka enables asynchronous communication between microservices by providing a durable, reliable, and distributed messaging system. Services can produce messages to Kafka topics without having to worry about the immediate consumer availability. This decouples services, allowing them to evolve independently and providing scalability and fault tolerance.

3. **Real-time Data Processing**: Kafka allows microservices to process real-time streams of data efficiently. Microservices can subscribe to relevant topics and consume data as soon as it becomes available, enabling real-time analytics, monitoring, and other data-driven capabilities.

4. **Fault Tolerance and Scalability**: Kafka provides fault tolerance by replicating messages across multiple brokers, thereby preventing data loss in case of failures. It also allows horizontal scalability by enabling the addition of new brokers to handle increased message throughput. This makes it suitable for highly available and scalable microservices deployments.

5. **Service Integration**: Microservices often need to integrate with various external systems, and Kafka serves as a central data hub that connects services with external systems. Services can consume and produce data from/to Kafka topics, allowing seamless integration with other systems.

Overall, Kafka acts as a flexible and scalable backbone for microservices architecture, facilitating effective inter-service communication, decoupling, event sourcing, real-time data processing, and integration with external systems. It enables a distributed, fault-tolerant, and scalable microservices ecosystem.

# Let's understand the key components of Kafka:

1. **Topics**: It is a category or feed name to which messages are published. Topics are divided into partitions for scalability and performance.

2. **Producers**: Producers are responsible for publishing messages to Kafka topics. They can be any application or system that generates data.

3. **Consumers**: Consumers read data from Kafka topics. They can be any application or system that processes or analyzes the data.

4. **Brokers**: Kafka brokers are the nodes that form the Kafka cluster. They handle the storage and replication of data across the cluster. Each broker contains one or more topic partitions.

5. **Partitions**: Topics are divided into partitions for scalability and parallelism. Each partition is an ordered, immutable sequence of messages. Each message within a partition is assigned a unique offset.

6. **Replication**: Kafka uses replication to provide fault tolerance and data durability. Each topic can have multiple replicas across different brokers, ensuring data availability in the event of a broker failure.

7. **ZooKeeper**: Kafka relies on ZooKeeper for coordinating and managing the brokers in a cluster. ZooKeeper helps with leader election, notification of changes, and maintaining cluster metadata.

In a typical setup, producers publish messages to Kafka topics by sending them to Kafka brokers. Brokers store the messages in their assigned partitions and replicate them across the cluster. Consumers subscribe to specific topics and partitions, read messages from the brokers, and process them as needed. ZooKeeper is used to maintain the cluster state and facilitate coordination between the brokers. Overall, Kafka provides a fault-tolerant, distributed, and scalable messaging system for handling high-throughput, real-time data streams.

# Kafka Setup and Configuration:

Installing and configuring Kafka on a local machine involves several steps. Here is a step-by-step guide for installing and configuring Kafka:

# Requirement:

> You will need to install the following package in your system to follow the next steps.

- Docker
- docker-compose


# first look at the docker-compose.yml file
This Docker Compose file is used to define and run multiple services and containers within a Docker environment. Let's break down each section:

1. `version: '3.3'`: This indicates the version of the Docker Compose file format being used.

2. `services`: This section defines the different services (containers) that will be created and run within the Docker environment.

- `zookeeper`: This service is based on the `wurstmeister/zookeeper` Docker image, which is an open-source ZooKeeper server.
  - `image: wurstmeister/zookeeper`: Specifies the Docker image to use for this service.
  - `container_name: zookeeper`: Sets the name of the container to "zookeeper".
  - `ports: - "2181:2181"`: Maps the host machine's port 2181 to the container's port 2181, allowing external access to the ZooKeeper server.

- `kafka`: This service is based on the `wurstmeister/kafka` Docker image, which is an Apache Kafka broker.
  - `image: wurstmeister/kafka`: Specifies the Docker image to use for this service.
  - `container_name: kafka_server`: Sets the name of the container to "kafka_server".
  - `ports: - "9092:9092"`: Maps the host machine's port 9092 to the container's port 9092, allowing external access to the Kafka broker.
  - `expose: - "9093"`: Exposes the container's port 9093 to other services within the same Docker network.
  - `environment`: Sets environment variables for the Kafka broker.
    - `KAFKA_ADVERTISED_HOST_NAME: kafka`: Sets the advertised hostname of the Kafka broker to "kafka".
    - `KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181`: Sets the connection string for ZooKeeper, which is in the format "hostname:port".
    - `KAFKA_AUTO_CREATE_TOPICS_ENABLE: 'false'`: Disables automatic topic creation by Kafka.
    - `KAFKA_CREATE_TOPICS: "my-topic-rk:1:1, my-topic-2:1:1"`: Specifies the creation of two topics with different partition and replica configurations.

- `producer` and `consumer`: These services are built using Dockerfiles located in the current context (specified by `context: .`). They both depend on the `kafka` service and are restarted in case of failure.
  - `container_name`: Sets the name of the containers.
  - `ports`: Maps the host machine's ports to the container's ports, allowing access to the services.


Note that this Docker Compose file assumes the presence of Docker images for ZooKeeper and Kafka (`wurstmeister/zookeeper` and `wurstmeister/kafka`, respectively) and Dockerfiles for the `producer` and `consumer` services.

# Next
> In the root directory, you'll see a file called server_up.sh, where I'll write this command.


- `docker-compose -f docker-compose.yml up --remove-orphans --build -d`

so just go to Terminal  and run this .sh file using the below command

> I'm writing the commands with `sudo` because I'm running Ubuntu on my system. You don't need sudo to write it.

- `sudo sh server_up.sh`

The configuration will create a cluster with 4 containers whose image name is :

- `zookeeper`
- `kafka_server`
- `Consumer`
- `Producer`


> To stop/kill these container, you can simply write a command in the terminal. 

- `sudo sh server_down.sh`

> Now we can check that our 4 container is running or not with the help of this command

- `sudo docker ps `

> to see the logs of these containers, simply type this command
- `sudo docker logs -f <container_id>`

we can see producer produce the messages from the dummy database and on the consumer terminal window, we can see that it consumes the messages from the Producer and then we insert the records into the Database.

That's it! You have now installed and configured Kafka on your local machine. You can explore more advanced Kafka configurations and features based on your specific use case.


# Now let's understand the purpose of Kafka topics and partitions and how does Kafka ensure fault tolerance through partitions?

The purpose of Kafka topics is to organize and categorize messages or records. Topics act as the central hub for data communication in Kafka. Producers write messages to a specific topic, and consumers read messages from topics of interest to them.

Partitions, on the other hand, are a way to divide a topic into smaller, ordered, and immutable sequences of messages. Each partition is a separate append-only log, and Kafka guarantees that messages within a partition are strictly ordered.

Kafka ensures fault tolerance through partitions by employing a concept called replication. When a topic is created, it can be configured with multiple replicas. Each partition has one leader and one or more follower replicas. The leader replica handles all read and write requests for the partition, while the follower replicas replicate the leader's log. In case of a leader failure, one of the followers is elected as the new leader. This replication mechanism ensures that even if a leader replica fails, the data and processing can continue with the newly elected leader.

The fault tolerance is achieved through the combination of partitioning and replication. By dividing a topic into partitions, Kafka can distribute the load across multiple brokers. Each partition also has multiple replicas spread across different brokers for redundancy. If one broker or replica fails, Kafka seamlessly switches to the replicas, maintaining data availability and ensuring fault tolerance. Additionally, by having replicas, Kafka allows data to be durably stored and prevents data loss in case of unexpected failures.

In summary, Kafka topics and partitions help organize and distribute data efficiently, and fault tolerance is ensured through replication, where multiple replicas of each partition are stored across different brokers.


























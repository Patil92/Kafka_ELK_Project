
Downloadd Kafka from Link
wget https://www-us.apache.org/dist/kafka/2.2.0/kafka_2.12-2.2.0.tgz -O kafka.tgz

tar -xzvf kafka.tgz --strip-components=1


Start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

Start Kafka
bin/kafka-server-start.sh config/server.properties


Create Kafka Topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic Patil92

To list topic Created 
bin/kafka-topics.sh --list --zookeeper localhost:2181

Kafka console Producer
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic Patil92

Kafka console Consumer
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Patil92 --from-beginning


Redis
redis-server  ==> starts server
redis-cli     ==> open's cli mode


ELK STACK
- installation and Configuration
    https://tecadmin.net/setup-elasticsearch-on-ubuntu/
    
    https://stackoverflow.com/questions/58656747/elasticsearch-job-for-elasticsearch-service-failed


To Know Physical and Virtual memory of Ubuntu
- https://askubuntu.com/questions/898941/how-to-check-ram-size


GitHub Pushing Data
 
 - create a new repository on the command line
    echo "# Kafka_ELK_Project" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/Patil92/Kafka_ELK_Project.git
    git push -u origin master

 - push an existing repository from the command line
    git remote add origin https://github.com/Patil92/Kafka_ELK_Project.git
    git push -u origin master



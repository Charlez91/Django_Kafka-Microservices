# Microservices with Django and Kafka
The project is a very basic microservice demonstration. It is made up of the UserService app which is like an app for `User` interactions. When a User registers it sends an event stream as a producer which is picked up by the Email Service App which then processes as a consumer and sends welcome email or whatever to onboarded users on successful registration. The LoggingService Logger then logs the event in the logs. Its implemented using Apache Kafka and Django

## Steps for setup.

* Make sure Java is installed on your machine. If not install from official sources. use to check
```bash
java --version
```

* Download and setup apache zookeeper from official sources

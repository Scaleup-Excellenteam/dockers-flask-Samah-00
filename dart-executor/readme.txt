to create a docker image run the following command:
docker build -t dart-executor-image .

to build a container run:
docker run -d -p 8003:8003 dart-executor-image

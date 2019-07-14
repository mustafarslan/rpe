# rpe
Rest API Performance Experiment


## Info

- Run MongoDB as Docker container image
```
    docker run -d -p 27017:27017 --name mongodb mongo
```

- Run Elastic Search as Docker container image
```
     docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.2.0
```

- Run Elastic Search as Docker container image with Dejavu Chrome plugin
```
    docker run -d --rm --name elasticsearch -p 9200:9200 -p 9300:9300 -e discovery.type=single-node -e http.cors.enabled=true -e http.cors.allow-origin=http://localhost:1358,http://127.0.0.1:1358 -e http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization -e http.cors.allow-credentials=true docker.elastic.co/elasticsearch/elasticsearch:7.2.0
```
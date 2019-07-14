# RPE-Backend
Rest API Performance Experiment

## Tech-Stack

### Backend
- Python
- Flask
- Flask Blueprint
- MongoDB as Docker image
- ElasticSearch as Docker image
- tqdm
- Flask-Cors
- Pandas

### Frontend
- Angular
- Angular Material
- Bootstrap
- Typescript
- PlotlyJS

## Prerequisite

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


## To run project with client

- For RPE Backend, install dependencies with following:

```python
    pip3 install -r requirements.txt
```

- For RPE Client, install dependencies with following:

``` 
    npm install
```

- RPE Backend uses MongoDB and Elastic Search as docker image. Please pull images as shown below
and then create container instances as shown above:

```
    docker pull mongo
    docker pull docker.elastic.co/elasticsearch/elasticsearch:7.2.0
```

( Once you have finished downloading images please, run container instances)

- Inside RPE Backend, for development purposes, under resources folder json file named "sample.json"
has been used. To use different json file please change your file name to "sample.json" and then
carry it under resources folder.

- To run RPE Backend , please run following command:

```python
    python3 server.py -h 0.0.0.0 -p 1080
```

- To store all the information inside json file in MongoDB, you are required to run following REST API
to commit each object to MongoDB

```
    GET http://localhost:1080/createdb
```

- You are required to sync all your data in MongoDB with Elastic Search Service, to do that
please run following REST API: 

```
    GET localhost:1080/synctoelastic
```

- Once RPE Backend operations are completed, you can start RPE Client by following command:

```
    npm start
```

- After RPE Client compilation is completed, on your browser, please go to following address:

```
    http://localhost:4200
```

- To test RPE application, please go through following options in order:
```
    - First, choose a date 
    - Second, choose a website name from dropdown menu
    - Finaly, click on Send button
```

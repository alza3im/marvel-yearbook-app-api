# marvel-yearbook-app-api

## Project prereq

Make sure you have docker-compose installed on your machine.


### Steps to get started
```
1. Start docker:

```
service docker start
```

2. Pull latest app docker image:
```
docker pull alza3im/marvel_api_flask:latest
```

3. Run container from above image:
```
docker run -it -p 5000:5000 --rm --name marvel-flask-app alza3im/marvel_api_flask:latest
```

NOTE: You might receive a 500 error, which might be due to having your domain not being added as an authorized device on marvel's developer account

### Backend is currently hosted on an AWS ec2 instance http://18.212.1.186:5000
```
Try the following endpoints

```
/name
/series
/comics
/stories
```

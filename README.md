# marvel-yearbook-app-api

## Project prereq

Make sure you have docker-compose installed on your machine.


### Steps to get started
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

NOTE: You might receive a 500 error, which might be due to having your domain not being
 added as an authorized device on marvel's developer account

### Backend is currently hosted on an AWS ec2 instance http://18.212.1.186:5000

Try the following endpoints

```
/name
/series
/comics
/stories
```

#### To do :
There's still a lot to be considred to do for this application to be production ready, 
the following is a simple to do list:

1. Add a data storage, which can be a postgresql with sqlalchemy (boiler-plate for a table is in models/)
as orm or Nosql such as mongodb.
2. Implement proper caching
3. Consider Asynchronisim for when we add more complex computations, i.e : Use Celery task queue to handle
long-running tasks.
4. In case we need to scale our application, Nginx can be utilized for load balancing as well as serving static files,
if we ever need to add any.

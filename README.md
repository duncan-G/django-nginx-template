<h1> Dockerzed Django + Nginx Boilerplate </h1>
<h3> About </h3>
<p>
A Dockerized Django 1.11 boilerplate with nginx as the reverse proxy meant to run on AWS with PostgreSQL on RDS and celery on Amazon SQS.
</p>
<p>
Make adjustments to .env file and place the correct credentials. </br>
To run locally (Will not start celery beat and worker):
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
```
For production
run `deploy.sh`. This will run the container in the background.
</br>
Otherwise run
```
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up
```


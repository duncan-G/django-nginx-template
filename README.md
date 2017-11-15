<h1> Dockerzed Django + Nginx Boilerplate </h1>
<h3> About </h3>

A Dockerized Django 1.11 boilerplate with nginx as the reverse proxy. This meant to run on AWS with PostgreSQL on RDS and celery on Amazon SQS.

Setup PostgreSQL DB on RDS and SQS queue. Make adjustments to .env file and place the correct AWS credentials. </br>
To run locally us `docker-compose.yml` (Will NOT start celery beat or worker):

``
docker-compose -f docker-compose.yml build
`` </br>
``
docker-compose -f docker-compose.yml up
`` </br>

For production

run `deploy.sh`. This will run the container in the background.
</br>


Otherwise run

``
docker-compose -f docker-compose-deploy.yml build
``  </br>
``
docker-compose -f docker-compose-deploy.yml up
``

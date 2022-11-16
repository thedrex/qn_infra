## this Dockerfile isn't used anywhere in our solution, but I included it as a toy example of how you might
## start incorporating this app into a pipeline that deployed to kubernetes or fargate instead of ec2.

from python:slim-buster

WORKDIR /app
COPY webserver/ /app
RUN pip install -r requirements.txt
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]
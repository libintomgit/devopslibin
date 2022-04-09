# syntax=docker/dockerfile:1

#down load the base image
FROM python:3.8-slim-buster

#argument variables for the docker file purpose
ARG user=appuser
ARG name=Libin

#Create new user
RUN useradd -ms /bin/bash ${user}

#change to user from root
USER ${user}

#global environment variable for the app
ENV MY_NAME=${name}

#create a directoy
RUN mkdir ~/${user}

#set the working directory in the container to /tom
WORKDIR ~/${user}

#copy file from the current directory of the Dockerfile to container current working directory /tom
COPY requirements.txt requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/home/${user}/.local/bin
#RUN echo "export PATH=~/${user}/.local/bin:$PATH" >> ~/.bashrc
#RUN export PYTHONPATH=~/${user}/.local/bin:$PYTHONPATH
# install the dependencies from the requirements.txt file
RUN pip3 install -r requirements.txt

#copy all files from the local directory to /tom in the container
COPY . .

#run python & flask locally
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

#RUN apt-get update
#CMD ["echo", "This is the first image from the dockerfile: Libin"]


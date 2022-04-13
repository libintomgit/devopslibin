# syntax=docker/dockerfile:1

#down load the base image
FROM python:3.8-slim-buster

#argument variables for the docker file purpose
ARG user=appuser
ARG name=Libin

#Create new user
RUN useradd -ms /bin/bash ${user}

# RUN apt --no-cache add curl
# RUN apt add --update curl && \
#     rm -rf /var/cache/apk/*
# # RUN curl --version
# RUN apt udpate
# RUN apt install -y curl

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

#set the env pythonpath for flask to work properly
ENV PYTHONPATH=$PYTHONPATH:/home/${user}/.local/bin

# install the dependencies from the requirements.txt file
RUN pip3 install -r requirements.txt

#copy all files from the local directory to /tom in the container
COPY . .


#run python & flask locally
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["--port= 5000"]

#RUN apt-get update
#CMD ["echo", "This is the first image from the dockerfile: Libin"]
# HEALTHCHECK --interval=5s --timeout=5s --start-period=2s --retries=2 \
#     CMD wget --no-verbose --tries=1 --spider http://localhost/tom || exit 1


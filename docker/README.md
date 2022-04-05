1. Lesson1 : Intro to docker
    - a container is standard unit of software that packages code and all its dependencies
    - Secure - major application process will be separate hence applications are secured
    - Scalable - 
    - Loosely coupled - 
    - SOA (service oriented architecture) a design philosophy that was popular decades ago
    - Docker Architecture
        - Docker client
            - docker users should use a client to communicate with docker.
            - docker client has ability to connect with several deamons
            - when a docker client executes a docker instruction, it sends it to the docker deamon which executes it
            - docker commands makes the use of docker API
        - Docker host
            - docker host offers a full environment in which applications can be executed and run
            - docker host consists of
                - docker daemon
                - imanges
                - containers
                - network
                - storage
            - docker daemon
                - docker clients interacts to docker deamon
                - the daemon accepts the command through CLI or REST API
                - docker daemon is incharge of all container related behaviour
            - images
                - are binary templates used to create containers
                - also provides metadata about the containers and its functionalities
                - image can be used to run container on its own or it can be modified to add additional elements to the current configuration
            - container registery
                - is the repo to store the docker images
                - registery can be setup in 2 diff ways
                    - private registery
                        - is used within an organisation
                    - public registery
                        - is used to share the images with the world
                - commands
                    - docker push
                        - is used to push the image to the registered registery
                    - docker pull
                        - is used to pull the image from the configured registery
                    - docker run
                        - creates a container using the image
            - containers
                - are encapsulated environments in whcih applications are run
                - they are determined and discribed by the factors configured like Network and Storage options
                - containers has access to the resource defined in the image, unless additional access mentioned while creating the container
                - a new image can be created based on the current state of a container
            - network
                - is the way for all the isolated containers to connect to one another
                - Primarily there are 5 network drivers
                    1. bridge
                        - is the container default network driver
                    2. host
                        - driver eliminates the netwrok barrier between the container and the docker host
                    3. overlay
                        - is used when the container has to be run on multiple docker hosts
                        - or multiple applications to form sworm services
                    4. none
                        - switches off all the networking options
                    5. macvlan
                        - gives containers a mac address to make them seem like a physical device
            - storage
                - we can store a data in a containers writable layer but we need driver 
                - there are 4 techneequs available for persistent data
                    1. data valume
                        - are stored on the host filesystem using a copy on write porcess
                        - that is reasonably efficient outside of the containers
                    2. volume containers
                        - hosting a volume in a dedicated container and mounting that volume to other containers
                    3. directory mounts
                        - another alternative to mount the local directory of a host into a container
                    4. storage plugins
                        - allows to link external storage system
                        - these pluggis move data from host to external storage

2. Lesson2: Docker fundamentals
    - docker components
        1. docker engine
            - works as a client - server model
            - client - is the command line utility that helps us to execute the command
            - server - docker engine works as the server, takes the input from the commond line, executes and gives the output
            - components of docker engine
                - docker daemon : Server
                    - is a process with a long running daemon process (dockerd)
                - CLI : Client
                    - will pass the instructions to the dockerd process
                - REST API : communication channel
                    - communication channel for the server and the client to interact
                - pluggis : is also major component and the plugins are available in various public registry
            - an administrator may configure set of conditions to represent the desires state
3. Lesson3: Getting started with docker
    - Remove previous version of docker
        - `docker, docker-engine, docker.io, containerd, runc`
        - the contents of `/var/lib/docker/` `/var/lib/containerd/` 
        - `sudo apt-get purge docker-ce docker-ce-cli containerd.io`    
    - pre-requsite
        - storage dirver
            - this driver allows you to create data in a writable layer of your container
            - supported storage drivers are
                - Overlay 2
                    - however this is the prefered storage driver for all the current supported linux distributions
                    - extra configuration is not required while using this driver
                - aufs
                - Btrfs
            - installtion on UBUNTU
                - update the current repository 
                - pre requsite packages to be installed - `ca-certificates, apt-transport-http, curl, lsb-release, gnupg`
                - download the docker gpg
                - download the stable repository package and install it
                - update the apt package
                - install the `docker-ce, containerd.io, docker-ce-cli` this will install the latest versions of the docker
                - check the previous versions - `apt-cache madison docker-ce`
                - use the `apt-get install docker-ce` with the version required
                - check if docker is working usign the `docker run hellow-world` command
                - install docker usign scrip
                    - download script from `curl -fsSL https://get.docker.com -o geL-docker.sh`
                    - run `sudo sh geL.docker.sh`
                - user sudo permission
                    - provide the user sudo permission for docker using the docker group
                    - `sudo usermod -aG docker <user-name>`
            - installtion on CENTOS
                - remove older version of docker
                    - `yum remove docker docker-client docker-client-latest docker-latest docker-common docker-engine docker-loglrotate docker-latest-logrotate`
                - pre-requesites
                    - centos version 7 or 8
                    - enable centos extras repository - this is enabled by default
                    - install the `yum install -y yum-utils`
                - using docker repository
                    - download the repository file
                    - update the repository `yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`
                    - put this file into /etc/yum.reposed/ and ensure that it is enabled
                    - `yum install docker-ce docker-ce-cli containerd.io`
                - using the shell script
                    - download the shellscriipt
                    - `curl -fsSL https://get.docker.com -o geL-docker.sh`
                    - run the script
                    
            
4. Lesson4: Build, Manage and distribute images
5. Lesson5: Container configuration
6. Lesson6: Networking
7. Lesson7: Orchastration
8. Lesson8: Container storage and volumes
9. Lesson9: Security


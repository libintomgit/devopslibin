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
    - docker client
        - docker client can be configured as well, using custom settings we can customise the own environment
        - using docker clint
            - pull the image
            - run container using the image
            - see the running containers
            - also manage the lifecycle of the container
        - popular docker client commands are
            - `docker build`
            - `docker pull`
            - `docker push`
            - `docker run`
    - docker server/host
        - is nothing other than a comute machine/system
        - it runs the docker daemon (dockerd)
        - multiple docker host is called docker cluster
    - configure docker environment
        - to use a different config file directory - use `DOCKER_CONGIG` environment variable to configure the new configuration directory
        - other way is to pass the `--config` in the command line itself (this is higher priority)
        - also use the export command to point the new locatoin of the configuration file
            - `echo export DOCKER_CONFIG=$HONE/new_direcory/.docker > ~/.profile` this will export the configuration file to the new directory structure and update the home profile with the new directory details
        - 2 ways
            1. config.json
                - which is the default docker configuration file
                - default configuration file location
                    - linux - `$home/.docker/`
                    - windows - `program data > Docker > Config > daemon.json`
            2. docker environment variables
    - docker registery
        - public registery
            - ex. docker hub
        - private registery
            - is hosted within the organisation and will be private for the organisation
    - docker images
        - is a kind of templete which is frozen in time with all the settings and required files (code, library, tools, dependencies) everything required to run an application
        - a docker images is multy layered storages which are being used as a one unit
        - it is possible to write on the layers only when the container is running
        - and next time when you write on it a new leyer will be created
        - summerise 
            - each container is an image, with a readable and writable layer on top of a bunch of read-only layer
            - all these layers generated when commands in the Dockerfiles are executed
            - or you modify while runnnign the container
        - each image will have different image ID and they are uniquely created
        - it is possible to create an imgae from the scratch (i.e, from the base image)
        - base image is the imgae used to create all the container image
    - docker file
        - is a collection of commands or instructions that can be used to build a docker image
        - inside a directory create a file with the naem Dockerfile (this is the unique name to be used to create)
        - Dockerfile format
            - add comment using #
            - directives are not case sensitive but bestpractice is to keep them in UPPERCASE to identify them easily
            - first have to write base image, that is from which image it will start and add the additional instruction (example installign a softeare on a base os image ubuntu)
            - FROM ubutnu - is the base imgae name
            - MAINTAINER Libin_Tom - is who manages it
            - RUN apt-get undate - is used to run the command
            - CMD `["echo", "this is the first image created by docker file : Libin]
    - docker build
        - `docker build` command builds the docker image using the Dockerfile
        - and the built image can be shipped to private or public registery
        - `docker run` is used to create container by specifiying that image
        - syntax `docker build [options] PATH or URL
        - if no input is provied by default docker bulid will look for the Dockerfile in the present directory
        - it builds the image from a docker file and its context.
            - context is the set of files located in the specified path or give url
        - .dockerignore file is used to exclude the file or directory while the docker build is running - this will increase the efficiency of the docker build
    - docker container lifecycle
        - process is
            - a running program that is currently executed in the system and a output generated from that process
            - a process can also have a child process/threads they are also an active process under one parent process
            - a process in a system can be started stopped killed
        - a container is nothing but a process
        - it can be started stopped killed
    - docker machine
        - is a utility which allows you to install docker engine on a remote host
        - also can manage the host using `docker machine` command
        - it also has ability to manage container (like start, stop, restart, inspect)
4. Lesson4: Build, Manage and distribute images
    - docker base image
        - is directed using `FROM` directive in the Dockerfile
        - then the base image is modified by the subsequent directives in the file
        - `FROM scratch/base_image_name` directive is used to create a image from the scratch
    - Dockerfile
        - https://docs.docker.com/language/python/build-images/
        - https://docs.docker.com/engine/reference/builder/
        - https://docs.docker.com/develop/develop-images/multistage-build/
        - `FROM 
        - `WORKDIR /any_directory` to set the current working directory
        - `VOLUME` - is used to get a persistant volume
        - `ENV` - setting the environment variable at the container level
            - Example:
            `ENV PYTHONPATH=$PYTHONPATH:/home/${user}/.local/bin`
        - `ADD` - is as similer as copy but in the add we can use http/s link
            - Example:
        - `ONBUILD` - is used to trigger the command when using this image as a base image
        - `STOPSIGNAL` - sends a system cal signal that helps the container to exit
        - `ENTYPOINT` - is a constant command which concatinated argument in the CMD or runtime
            - Example:
            `ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]`
            `CMD ["--port= 5000"]`
        - `HELTHCHECK` - will check and exit the container based on the command conditions
            - Example:
            `HEALTHCHECK --interval=5s --timeout=5s --start-period=2s --retries=2 \`
                `CMD wget --no-verbose --tries=1 --spider http://localhost/tom || exit 1`
    - own registery
        - docker run -d -p 5000:5000 --restart-yes --name registry registry:2
        - will be hosted on-prem and the images can be pushed using the same
        - docker push 192.168.1.39:5000/python_app:v1.0
    - Clean docker
        - 
5. Lesson5: Container configuration
6. Lesson6: Networking
    - docker engine utilises linux namespace for to run the container
    - linux network namespace cteates a isolated namespace which will contain vnet, ARP table and ROUTE table
    - 3 network that docker creates are
        - bridge network
            - by default when you run a docker container it attachts to the beidge network
                - when docker is installed docker engine will create a bridge network (like VNet) with the ip 172.17.0.1
                - which means it will create its own namespace, attach the name space to the default bridge netwokr of the docker
                - with the IP from the IP pool assign to the bridge netwok
                - which means a new linux network namespace is created for the container and the veth is linked to the bridge network by the docker engine
                - 
        - host network
            - is a network where we can run ony one container in specific port
            - which means, the host and the continer port will be tightly coupled so the port of the container will the port of the host
        - none network
            - that container is isolated in nature and it will not connect to any network
            - in kubernets this concept is used because in k8s different network providers are used (like calico, flwnel) and they need the basic container network to be NONE connet the containers to the different network
    - custom/ user defined newtorking
        - it is possible to create user defined multiple bridge networks with user defiled CIDR range and choose which bridge the container should run on
        - `docker network create --driver bridge --subnet 182.18.0.0/16 custom-isolated-network`
          `docker network ls`
        - command to connect and disconnect the container to different custome network
            - `docker run -d <image_name> --network <custom_network>`
            - `docker network connect <network-name> <container-name>`
            - `docker network disconnect <network-name> <container-name>`
            - `docker network prune or docker network rm <network-name>`
    - DNS
        - DNS container is created while installing the dokcer engine
        - and its usually present on 127.0.0.11 IP
        - and the name entry of the continer is created in the DNS server

8. Lesson8: Container storage and volumes
    - when docker engine is installed it created a directory in /var/lib/docker
    - this is where all over persistant data gets stored
    - layers
        - image layer
            - so docker says, what ever the layer that we build at the image layer or the build layer, those are always read-only in nature and they cannot be over written when the container launches
            - and those data will be always available
        - container layer
            - is read/write layer and changes can be made while running the container
            - container layer will be on the memory (RAM)
    - create a volume 
        - mount
            - when you map your volume to the container directory its called mount
            - using `docker volume create <volume_name>`
            - this will create a volume directory in the /var/lib/docker/volumes directoy
            - however you can use any directory as a voume in the Dockerfile and if the directory is not present then the docker will create one while running
            - `docker run -v <volume_name>:<container/container>`
        - bind
            - when you map the host path to the container path its called bind(ing)
            - `docker run -v <host/path>:<container/container>`
            - and in latest version on the docker --mount is used in the place of -v
            - `docker run --mount type=bind, source=<path/of/host/directory>, target=<path/to/container/directory>`


9. Lesson9: Security
8. Lesson00: Docker Compose
    - create a docker compose file
    - run the compose using `docker-compose up`
    - syntax - Version 2
    ``` version: 2
        services:
            name_of_the_container:
                image: <image_name>
                or
                build: ./<docker_file_directory> #this builds the image from the docker file and then runs the container
                ports:
                    - <host>:<container>
                depends_on:
                    - <other container name>
                networks:
                    - front-end
                    - back-end
        
        network:
            front-end
            back-end ```
        - 
7. Lesson7: Orchastration
    - in any kind of orchastration whats first needed is cluster (cluster is collection of nodes)
    - out of the custer one of the node will be management/master node
    - docker swarm
        - `docker swarm init --advertise-addr 192.168.33.30` to initiate the controller in the master node 
        - `docker system info` will provide the information of the docker master
        - after the init, using the `docker sworm join` command join the other nodes to the cluster
        - ```docker swarm join --token SWMTKN-1-60dgglp1o6kdyz7v4mu9iu70ynn9713334fseymua0umx7enob-3s46u1nfvbtkug5bkzfxa4zhh 192.168.33.30:2377```
        - `docker swarm join-token manager`
        - check the list of nodes using `docker node ls`
        - availability
            - active - running and accepting the new containers
            - pause - not available to take the new containers
            - drain - is to take down the node. So it shcedules the existing containers in other nodes and terminates the containers in the node.
        - manager status
            - leader: is the active manger, who is the controle plane
            - reachable: comes in picture when the multi manager senario
            - unreachable: at a point of time only one node will be manager and hence reachable and unavailable comes in that picture
        - inspect the node details `docker node inspect <nodename> --pretty`
        - promote worker as the manager `docker node promte <workernodename>`
        - demote manager as the worker `docker node demote <workernodename>`
        - drain the node `docker node update --availability drain <nodename>`
        - activate back from drain status `docker node update --availability active <nodename>`
        - when the drained noded comes active the old workloads will not be reschduled to the node
        - leave the worker node from the cluster. First drain the node then within the worker node leave the docker swarm `docker swarm leave`
        - remove the node entry `docker node rm <node_name>`
        - get the cluster join token again ` docker swarm join-token worker`
    - #docker swarm operations
        - create service `docker service crate --replicas=3 <imagename>`
        - list services running `docker service ls`
        - list the pods running in a particular service `docker service ps <service_name>`
        - print the service details `docker service inspect <service_name> --pretty`
        - check logs of service `docker service logs <service_name>`
        - servicer rolling updates
            - update the image immediately in all the containers`docker service update -p 80:80 --image=<image_name:new_version> <old_image>`
            - update the images with delay ```docker service update -p 80:80 --update-delay 60s --image=<image_name:new_version> <old_image>```
            - update parallaly for faster update ```docker service update -p 80:80 --update-parallelism 3 --image=<image_name:new_version> <old_image>```
            - update failure situation ```docker service update -p 80:80 --update-failure-action <pause or continue or rollback> --mage=<image_name:new_version> <old_image>```
            - rolling back `docker service update --rollback <image_name>`
            - update replicas `docker service update --replicas=<desired_number> <service_name>`
            - daemon set `docker service create --mode=global agent`
        - lables & constraints
            - add lables to the nodes `docker node update --lable-add <lable-ex-type=cpu-optimised/type=memory-optimised> <worker_node1>`
            - and add contraint while running the service ```docker service create --constraint=node.lables.type==cpu-optimized <service_name>```
        - network - overlay2
            - while initialising the swarm it creates two network
                - overylay (ingress)
                    - is spanned accross the entire cluster
                    - which allows communication between all the containers
                    - this concept is called ROUTING MESH
                    - create a custom overly network `sudo docker network create -d overlay <network_name>`
                - default network (bridge)
                    - is used to connect nodes in the cluster
        - service recovery
        - Quorum
            - concept: when ever the mangaer going to take any decicion, depending on the number of managers there is one particular number should agree your decicion inorder to form a quorum only then the request id effective
            | MANAGERS | MEJORITY | FAULT TOLLARANCE |
            | 1 | 1 | 0 |
            | 2 | 2 | 0 |
            | 3 | 2 | 1 |
            | 4 | 3 | 1 |
            | 5 | 3 | 2 |
            | 6 | 4 | 2 |
            | 7 | 4 | 3 |

            - above is the list which says how many managers should agree in minimum to execute a request and if the minimum managers are not reachable then the request will not be processed.

            - quorum N = n / 2 + 1 and decimal to round up to least.
            - docker reccomends 7 managers max as the any more would give the high availability of only 7 managers
10. Docker Stack:
    - https://github.com/dockersamples/example-voting-app.git
    - `docker stack deploy --compose-file docker-compose.yml`
11. Kubernetes
    - Master: 4 specific components which will do the job of end to end orchestration
        - kube-API:
            - any request will come through the kube api server route
            - admin can connect to the master through CLI kubectl or REST API
            - it is a facilitator
            - it receives the user requests, authenticates and validates
            - once done writes into the etcd
            - then gives the instructions to schedular
            - once the schedular reverts with the decision information, it provides the same back to controller
            - API then sends the controller processed request to KUBELET
        - etcd
            - only database in the k8 cluster
            - highly distributed key value pair
            - 
        - schedular
            - continuesly checks with the kube api for any new request/ job
            - it is the decision maker as such to whihc node the pods should be created based of the node helth and raning
            - once the decision is made, it forwards the information back the API
        - controller
            - is the brain of the k8s
            - it received the instruction from the API which was earlier processed by the schedular
            - it checks for the actual implementation proceedure and sends back to API
            - 
    - Worker: 3 components
        - kublet
            - is the captain of the worker node
            - has all the status of the worker node
            - receives the instructions from the api server which shceduler and controller earlier processed
            - then it instructs the container run time to process the actual requirement
        - kube-proxy
        - container runtime (docker engine/ rocker engine/ crio engine / etc.)
    - pod
        - is the smallest deployable unit in the k8s
        - 99% the pod will contain single container but it can contain many containers
        - one main container should be in one pod 
        - `kubectl run pod --image <image_name>`
        - `kubectl get pods`
    - replica set
        - will delcleratively create the pod with replicas and maintains the desired state (self healing)
        - rolling upadte is not available
    - deployment
        - includes replicaset and rolling update
        - `kublectl apply -f <deployment_file.yaml>` run the deployment decleratively
        - `kubectl get deployments` list the deployments in the cluster
        - `kubectl describe deployment <deployment_name>` show the details of the deployment
        - `kubectl rollout status deployment <deployment_name>` to rollout the new version
        - `kubectl rollout history deployment <deployment_name>` check the rollout history
        - `kubectl set image deployment <deploymetn_name> <old_image:version=ne_image:version>` rollout the image imperatively     
        - `kubectl rollout undo deployment <deployment_name>` rollback to the previous revision
        - `kubectl rollout undo deployment <deployment_name> --to-revision=2` undo to particular revision image
    - services
        - node port:
            - will get a public port
            - 
        - cluster IP:
            - works within the cluster
            
        - loadbalancer:
            - will balance the tarffick from node point
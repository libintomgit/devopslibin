<h1>Part 1 of the assignment - Run the csvserver container and browse through localhost:9393</h1>

**Pull the container image for csvserver**

`docker pull infracloudio/csvserver:latest`

**Run the image with basic arguments**

`docker run --name csvserver3 -d infracloudio/csvserver:latest`

**check if the cocntainer is running**

`docker ps`

**if the container is not running check the all list**

`docker ps -a`

**using the container name or id grep for log path**

`docker inspect f1c4e0c521d3 | grep Log`

**check the log for possible error**

`cat /var/snap/docker/common/var-lib-docker/containers/f4c5e1c522d3299193cae71b5126937be003c8913e2f93f728fc95134a8e3eb5/f1c4e0c521d3299192cae69b5126935be003c8913e2f93f728fc95134a8e3eb5-json.log`

*it is understood that the application is looking for a file called inputdata and which needs to be created and mounted*

**mount the generated file to the file name coded in the application and run the container again**

`docker run -d --name csvser2 -v $(pwd)/inputFile:/csvserver/inputdata infracloudio/csvserver:latesti`

**bash to the running container to identfy the application listning port** 

`docker exec -it csvser1 bash`

**run the netstat command inside the container to find the application listning port**
*this can be found in the `docker ps` too*

`netstat -punta`

**stop and delete the container**

`docker stop csvser1
 docker rm csvser1`

**run the container again by exposing the port to 9393 and CSVSERVER BORDER environmental variable set to Orange**
 
`docker run -d --name csvser1 -v /home/libin/ic_assignment/ic_assignment/solution/inputFile:/csvserver/inputdata -p 9393:9300 -e CSVSERVER_BORDER=Orange infracloudio/csvserver:latest`



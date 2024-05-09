##Update the repository
`sudo apt-get update`

##turn off the swap
`swapoff -a`

##remove swap entry from the fstab for the parmanent removal
`/etc/fstab`

##update the hostname 
`sudo hostname <new_hostname>`
or edit
`/etc/hostname`

##set the static ip address 
`vi /etc/network/interfaces`
> auto enp0s8
>   iface enp0s8 inet static
>       address 192.168.33.40
>       netmask 255.255.255.0

##update the ip in the hosts file with the hostname
`vi /etc/hosts`
`192.168.33.40 kubemaster1`

##Install openssh-server if its not already installed
`sudo apt-get install -y openssh-server`

##Install docker container runtime
update the repo first
`sudo apt-get updat`
`sudo apt-get install -y docker.io`

##Install Curl and Apt-transport-https
`sudo apt-get update && sudo apt-get install -y apt-transport-https curl`

##Add the apt key for kubernets
`sudo su`
`curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -`

##Add the kubernets source list
```
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
```
##update the repo again
`apt-get update`

##Install Kubeadm, kubelet and kubectl
`apt-get install -y kubelet kubeadm kubectl`

##Change the configuration file of Kubernetes
`vi /etc/systemd/system/kubelet.service.d/10-kubeadm.conf`
update the below environment variale at the last lastline
this will update the cgroup driver to systemd or cgroupfs
`Environment=”cgroup-driver=systemd/cgroup-driver=cgroupfs”`

##Update the docker.json
`echo '{"exec-opts": ["native.cgroupdriver=systemd"]}' >> /etc/docker/daemon.json`
`systemctl restart docker`

#Only kubernetes master

##Initialize the kubernets cluster
`kubeadm init --apiserver-advertise-address=192.168.33.40 --pod-network-cidr=192.168.0.0/16`

##Save the join command for later use in the worker nodes
>kubeadm join 192.168.33.40:6443 --token j4b2ly.10pn9ic6dwp7p6fa \
>       --discovery-token-ca-cert-hash sha256:9bd3425b1957071a1ebd96850688b4e1995bf0551228710fe26dd11c62ffe391

##Now run the following commands
as instructed by the kubeamd on the screen in the output of the init command
SWITCH TO REGULAR USER
cteate directory in the user home
`mkdir -p $HOME/.kube`
copy kubernets admin.conf file to newdirectoy at home
`sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config`
change the newdirectory ownership to the current user
`sudo chown $(id -u):$(id -g) $HOME/.kube/config`

##Check if kubernets is working
`kubectl get pods -o wide --all-namespaces`

##Install the POD network
this will run the calico network pod from the project calico
download the calico manifest
`curl https://projectcalico.docs.tigera.io/manifests/calico.yaml -O`
apply the configuration
`kubectl apply -f calico.yaml`

##Check if the pods are working now
`kubectl get pods -o wide --all-namespaces`

##Install the kubernets dashboard
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.0/aio/deploy/recommended.yaml`

#Only kubernetes worker nodes


--------------------------------------------------------------------------
kube

* Create Deployment explecitly
kubectl create deployment bmt-fe --image=libintomdocker/bookmytable-frontend

* Create service to expose the deployment
kubectl expose deployment bmt-fe --type=NodePort  --port=8000 --target-port=8000

* Export the deployment to yaml configuration >
kubectl get deployment <deployment-name> -o yaml > <file-name>.yaml

* Export the service to yaml configuration >
kubectl get svc bmt-fe -o yaml > service-fe.yaml



#Bookmytable - Frontend
docker run -p 8000:8000 --name bmt-fe --network bmt-network -e BACKEND_URL=http://bmt-be:8005/api libintomdoc
ker/bookmytable-frontend

#Bookmytable - Backend
docker run -d -p 8005:8005 --name bmt-be --network bmt-network -e POSTGRES_PASSWORD=postgres123  libintomdocker/bookmytable-backend:latest

#Bookmytable - Postgres
docker run --name bmt-postgres --network bmt-network -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres123 -e POSTGRES_DB=bmtbkenddb1 postgres


apiversion: apps/v1
kind: Deployment
metadata:
    name:
    lable:
    namespace:
spec:
    replicas:
    selector:
        matchLabels:
    template:
        metadata:
            lables:
        spec:
            containers:
            - name:
              image: 
              imagePullPolicy:
            restartPolicy:




    stratergy:

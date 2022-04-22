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

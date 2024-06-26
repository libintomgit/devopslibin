## Commands
### Login to argocd cli
(server ip and port in the case of running in k8s cluseter service ip and port)

`argocd login  192.168.49.2:30809`

### Creating project
server details followed by the namespace if specific to a namespace
`argocd proj create devops-tools -d https://kubernetes.default.svc,devops-tools`

`argocd proj add-destination <PROJECT> <CLUSTER>,<NAMESPACE>`

`argocd proj remove-destination <PROJECT> <CLUSTER>,<NAMESPACE>`

Nagatiation

`argocd proj add-destination <PROJECT> !<CLUSTER>,!<NAMESPACE>`

`argocd proj remove-destination <PROJECT> !<CLUSTER>,!<NAMESPACE>`

### Adding and removing permitted git repo to a project
`argocd proj add-source <PROJECT> <REPO>`

`argocd proj remove-source <PROJECT> <REPO>`

### Adding and removing Nagation (denaial) git repo to a project
`argocd proj add-source <PROJECT> !<REPO>`

`argocd proj remove-source <PROJECT> !<REPO>`





helm delete elastic-libin -n devops-tools

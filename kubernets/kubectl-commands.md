### Checke the existing namespace
kubectl config view --minify | grep namespace

### Checkout the namespace
kubectl config set-context --current --namespace=namespace

### Copy files from host to container
kubectl cp <src-path> <your-pod-name>:<dest-path> 

### Copy files from container to host
kubectl cp <your-pod-name>:<src-path> <local-dest-path> 
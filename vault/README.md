https://github.com/shabbirsaifee92/vso-demo/blob/main/vault-auth.yaml

## Install hashicorp vault using the helm repo

This will start a vault dev server, so there is no need to unseal the vault server as we do in prod

`helm install vault hashicorp/vault -n vault --create-namespace --set server.dev.enables=true`

This is the command to install the vault in production mode, hence this needs to be unsealed to start the server.

`helm install vault hashicorp/vault -n vault --create-namespace`

## NOTE
1. vault use environment variables for the server address and many other configurations
    VAULT_ADDR

## Initialize vault

`vault operator init`

## Unseal the vault within the vault-0 pod (statefulset)
Do this 3 time with different key pinted at the time of vault operator init

`vault operator unseal`

## Login to vault to authenticate with token for further access

`vault loing -method token token="token_provided_in_the_init"`

## Enable KV-V2 Secret engine ( Key Value)

`vault secrets list`

`vault secrets enable kv-v2`

## Create new secret

`vault kv put kv-v2/k8s/libinsecret username=libintom`

#### View the secret

`vault kv get kv-v2/k8s/libinsecret`

## Create policy

`vault policy list`

```
vault policy write libinsecret - << EOF
path "kv-v2/k8s/libinsecret" {
    capabilities = ["read"]
}
```
## Create role

```
vault write auth/kubernetes/role/libin-role bound_service_account_names=default bound_service_account_namespaces=default policies=default,libinsecret audience=vault ttl=1h
```
creates a libin-role in kubernetes/role

plicies applies the default and previously created policy libinsecret

Here the audience is JWT concept, where anyother service than vault will be rejected

## Enable Kubernetes authentication

`vault auth list`

`vault auth enable kubernetes`

## Configure to communicate with Kubernetes API server

This method is used while we want to fetch the vault secret directly into the pod (with out vault secrets operator)

`vault write auth/kubernetes/config kubernetes_host=https://$KUBERNETES_SERVICE_HOST:$KUBERNETES_SERVICE_PORT`

Success! Data written to: auth/kubernetes/config

Kubernetes by default adds KUBERNETES_SERVICE_HOST and KUBERNETES_SERVICE_PORT environment variables to the PODS

## Configure to communicate with Kubernetes API server (for Vault Secrets Operator)

`vault write auth/kubernetes/config kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443"`

Success! Data written to: auth/kubernetes/config

## Install Vault Secret Operator

`helm install vault-secrets-operator hashicorp/vault-secrets-operator -n vault-secrets-operator-system --create-namespace`





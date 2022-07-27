#TERRAFORM CONFIGURATION

##Creating teraform basic structure and commands
- create the configuration
  - create a directory
  - file with .tf extention
  - then enter the code in the .tf file
  - run `terraform init`
    - this will initialise all the providers
  - run `terraform plan`
    - will provide all the plan of action written in the file
  - run `terrform apply`
    - which will then do the execution to make the changes to the infrastructure as per the plan

##Creating a docker container using terraform
(in a local computer)

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

terraform { 
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    } 
  }
}
    
source = provider pluggin
version = provider pluggin name version

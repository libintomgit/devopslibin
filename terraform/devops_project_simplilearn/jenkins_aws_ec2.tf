terraform {
  backend "remote" {
    organization = "abc"
    workspaces {
      name = "jenkins"
    }
  }
}

provider "aws" {
  region                  = var.region
  shared_credentials_file = var.credentials_file
  profile                 = var.profile
  default_tags {
    tags = {
      DEPARTMENT = var.department
      PROJECT    = var.project
    }
  }
}


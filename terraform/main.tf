# Configure AWS
provider "aws" {
  region = "us-east-1"
}

module "iam_user" {
  source = "github.com/cisagov/molecule-packer-travisci-iam-user-tf-module"

  ssm_parameters = ["/vnc/username", "/vnc/password"]
  user_name      = "test-ansible-role-vnc-server"
  tags = {
    Team        = "NCATS OIS - Development"
    Application = "ansible-role-vnc-server testing"
  }
}

(terraform-tutorial)=
# Deploying CrateDB to the cloud using Terraform

## Introduction

CrateDB already has a wide variety of deployment options, ranging from
{ref}`docker-compose` to {ref}`cloud setups <install-cloud>` on AWS and Azure.

To make cloud setups more manageable and predictable, we today add another
option using [Terraform], an infrastructure-as-code tool.
Terraform eliminates the need to create resources manually via the cloud console.
Instead, it is based on a configuration language describing resources based
on a given parametrization.

## Example

The example below shows a 3 node cluster across several availability zones on AWS.
Currently, AWS and Azure are supported as target platforms.
The setup for Azure is very similar, please see the [README].

## Configuration

First, we create a new Terraform configuration file named `main.tf`.
That file references the [crate/crate-terraform](https://github.com/crate/crate-terraform) repository with the underlying logic of the deployment. Several variables need to be specified regarding the target environment.


```hcl
module "cratedb-cluster" {
  source = "git@github.com:crate/crate-terraform.git//aws"

  # Global configuration items for naming/tagging resources
  config = {
    project_name = "example-project"
    environment  = "test"
    owner        = "Crate.IO"
    team         = "Customer Engineering"
  }

  # CrateDB-specific configuration
  crate = {
    # Java Heap size in GB available to CrateDB
    heap_size_gb = 2

    cluster_name = "crate-cluster"

    # The number of nodes the cluster will consist of
    cluster_size = 3

    # Enables a self-signed SSL certificate
    ssl_enable = true
  }

  # The AWS region
  region = "eu-central-1"

  # The VPC to deploy to
  vpc_id = "vpc-1234567"

  # Applicable subnets of the VPC
  subnet_ids = ["subnet-123456", "subnet-123457"]

  # The corresponding availability zones of above subnets
  availability_zones = ["eu-central-1b", "eu-central-1a"]

  # The SSH key pair for EC2 instances
  ssh_keypair = "cratedb-cluster"

  # Enable SSH access to EC2 instances
  ssh_access = true
}

# Connection information on the newly created cluster
output "cratedb" {
  value     = module.cratedb-cluster
  sensitive = true
}
```

## Execution

Once all variables are adjusted, we initialize Terraform by installing needed plugins:

```bash
$ terraform init   
Initializing modules...
Downloading git@github.com:crate/crate-terraform.git for cratedb-cluster...
- cratedb-cluster in .terraform/modules/cratedb-cluster/aws

Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/random versions matching "~> 3.1"...
- Finding hashicorp/tls versions matching "~> 3.1"...
- Finding hashicorp/aws versions matching "~> 3.0"...
- Finding hashicorp/template versions matching "~> 2.2"...
- Installing hashicorp/tls v3.1.0...
- Installed hashicorp/tls v3.1.0 (signed by HashiCorp)
- Installing hashicorp/aws v3.61.0...
- Installed hashicorp/aws v3.61.0 (signed by HashiCorp)
- Installing hashicorp/template v2.2.0...
- Installed hashicorp/template v2.2.0 (signed by HashiCorp)
- Installing hashicorp/random v3.1.0...
- Installed hashicorp/random v3.1.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

[...]
```

Before deploying anything to the cloud, we can optionally print the planned resource creation that Terraform derived from the configuration (the output below is shortened):
```bash
$ terraform plan   

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
 <= read (data resources)

Terraform will perform the following actions:

  # module.cratedb-cluster.aws_instance.cratedb_node[0] will be created
  + resource "aws_instance" "cratedb_node" {
      + ami                                  = "ami-0afc0414aefc9eaa7"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = "eu-central-1b"
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t3.xlarge"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = "cratedb-cluster"
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Environment" = "test"
          + "Name"        = "example-project-test-node-0"
          + "Owner"       = "Crate.IO"
          + "Team"        = "Customer Engineering"
        }
      + tags_all                             = {
          + "Environment" = "test"
          + "Name"        = "example-project-test-node-0"
          + "Owner"       = "Crate.IO"
          + "Team"        = "Customer Engineering"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification {
          + capacity_reservation_preference = (known after apply)

          + capacity_reservation_target {
              + capacity_reservation_id = (known after apply)
            }
        }

      + ebs_block_device {
          + delete_on_termination = true
          + device_name           = "/dev/sdh"
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + snapshot_id           = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = 512
          + volume_type           = (known after apply)
        }

      + enclave_options {
          + enabled = (known after apply)
        }

      + ephemeral_block_device {
          + device_name  = (known after apply)
          + no_device    = (known after apply)
          + virtual_name = (known after apply)
        }

      + metadata_options {
          + http_endpoint               = (known after apply)
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = (known after apply)
        }

      + network_interface {
          + delete_on_termination = false
          + device_index          = 0
          + network_interface_id  = (known after apply)
        }

      + root_block_device {
          + delete_on_termination = true
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = 50
          + volume_type           = (known after apply)
        }
    }

  # module.cratedb-cluster.aws_instance.cratedb_node[1] will be created
  + resource "aws_instance" "cratedb_node" {
        [...]
    }
    [...]
}
```

If the plan looks fine, the last step is executing the plan:

```bash
$ terraform apply  

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
 <= read (data resources)

Terraform will perform the following actions:

[...]

Apply complete! Resources: 22 added, 0 changed, 0 destroyed.

Outputs:

cratedb = <sensitive>
```

## Connecting to CrateDB
The `cratedb` output element contains information on the newly created cluster, such as URL and credentials. Since it contains the admin password, the output is marked as sensitive and not immediately shown by Terraform. It can be made visible via the `terraform output` command:
```bash
$ terraform output cratedb
{
  "cratedb_application_url" = "https://example-project-test-lb-572e07fbd6b72b88.elb.eu-central-1.amazonaws.com:4200"
  "cratedb_password" = "IgqVcBV28wNX8Js1"
  "cratedb_username" = "admin"
}
```

## Teardown

If you no longer need the deployed cluster, a simple `terraform destroy` from the same directory will suffice.

```bash
$ terraform destroy
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # module.cratedb-cluster.aws_instance.cratedb_node[0] will be destroyed
  - resource "aws_instance" "cratedb_node" {
       [...]
        } -> null

Plan: 0 to add, 0 to change, 22 to destroy.

Changes to Outputs:
  - cratedb = (sensitive value)

[...]

Destroy complete! Resources: 22 destroyed.
```

For optimal security, a self-signed SSL certificate was automatically generated and deployed. After adding an exception in your browser to accept the certificate, the HTTP Basic Auth dialog of CrateDB’s Admin UI will show. Authenticate with the credentials retrieved from above.

If the credentials are rejected, or no authentication prompt appears, please wait for a couple of minutes and try again. Provisioning the virtual machines might not be complete yet and can take several minutes.

## Final Remarks

Please note that (as of now) the provided Terraform configuration is meant for development or testing purposes and doesn’t fulfill all requirements of a production-ready setup (i.e. regarding high availability, encryption, or backups). For production-ready setups, please consider [CrateDB Cloud](https://crate.io/products/cratedb-cloud/).

If you have any feedback or requests to extend the configuration, please feel free to [open an issue on GitHub](https://github.com/crate/crate-terraform/issues) or let us know in this thread!


[README]: https://github.com/crate/cratedb-terraform/blob/main/azure/README.md
[Terraform]: https://www.terraform.io/

(terraform-usage)=
# Deploying CrateDB to the cloud using Terraform

## Introduction

CrateDB offers multiple deployment options, from {ref}`docker-compose` to
{ref}`cloud setups <install-cloud>` on AWS and Azure.

To make cloud setups more manageable and predictable, this guide presents
another option using [Terraform], an infrastructure-as-code tool.
Terraform eliminates manual console steps to create resources.
Instead, Terraform uses a configuration language that describes resources
with parameters.

## Prerequisites

- Terraform CLI >= 1.5
- An AWS account with credentials configured (AWS SSO/profile or env vars)
  and a default region or the provider block shown below
- Existing VPC and subnet IDs in the chosen region (and their AZ mapping)
- An EC2 key pair name to use for SSH
- jq installed (used to pretty‑print JSON output)

## Example

This example deploys a 3‑node cluster across multiple Availability Zones on AWS.
The module currently supports AWS and Azure.
For Azure, see the [README].

## Configuration

First, create a Terraform configuration file named `main.tf`.
Reference the [cratedb-terraform] module, which contains the deployment logic.
Then, specify variables for the target environment.

```hcl
terraform {
  required_version = ">= 1.5.0"
}
variable "region" {
  type    = string
  default = "eu-central-1"
}
provider "aws" {
  region = var.region
}
module "cratedb_cluster" {
  source = "https://github.com/crate/cratedb-terraform.git//aws"

  # Global configuration items for naming/tagging resources
  config = {
    project_name = "example-project"
    environment  = "test"
    owner        = "Crate.IO"
    team         = "Customer Engineering"
  }

  # CrateDB-specific configuration
  crate = {
    # Java heap size in GB available to CrateDB
    heap_size_gb = 2

    cluster_name = "crate-cluster"

    # Number of nodes in the cluster
    cluster_size = 3

    # Enable a self-signed TLS certificate
    ssl_enable = true
  }

  # AWS region
  region = var.region

  # Target VPC
  vpc_id = "vpc-1234567"

  # Subnets in the VPC
  subnet_ids = ["subnet-123456", "subnet-123457"]

  # Availability Zones for the subnets above
  # Note: AZ suffixes are account-specific; ensure these match your subnets' AZs.
  availability_zones = ["eu-central-1b", "eu-central-1a"]

  # SSH key pair name for EC2 instances
  ssh_keypair = "cratedb_cluster"

  # Enable SSH access to EC2 instances
  # Tip: restrict SSH to your IP/CIDRs if supported by the module.
  ssh_access = true
}

# Connection information for the newly created cluster
output "cratedb" {
  value     = module.cratedb_cluster
  sensitive = true
}
```

## Execution

Once you adjust all variables, initialize Terraform by installing the needed plugins.
```bash
$ terraform init   
Initializing modules...
Downloading git::https://github.com/crate/cratedb-terraform.git for cratedb_cluster...
- cratedb_cluster in .terraform/modules/cratedb_cluster/aws

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

Before deploying, optionally print the planned resource creation derived from the
configuration (shortened output below):
```bash
$ terraform plan   

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
 <= read (data resources)

Terraform will perform the following actions:

  # module.cratedb_cluster.aws_instance.cratedb_node[0] will be created
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
      + key_name                             = "cratedb_cluster"
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

  # module.cratedb_cluster.aws_instance.cratedb_node[1] will be created
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

## Connect to CrateDB

The `cratedb` output element contains the connection details (URL and
credentials). Because it’s marked sensitive, human‑readable output is
redacted. Use the `terraform output` command to display it, adding
`-json` to print the full value and pipe it to `jq` (ensure `jq` is
installed).
```bash
$ terraform output -json cratedb | jq
```
```json
{
  "cratedb_application_url": "https://example-project-test-lb-572e07fbd6b72b88.elb.eu-central-1.amazonaws.com:4200",
  "cratedb_password": "IgqVcBV28wNX8Js1",
  "cratedb_username": "admin"
}
```

## Teardown

:::{caution}
The next steps will create billable AWS resources. Destroy the stack when finished
to avoid ongoing costs.
:::

If you no longer need the deployed cluster, a simple `terraform destroy` from
the same directory will suffice.

```bash
$ terraform destroy
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # module.cratedb_cluster.aws_instance.cratedb_node[0] will be destroyed
  - resource "aws_instance" "cratedb_node" {
       [...]
        } -> null

Plan: 0 to add, 0 to change, 22 to destroy.

Changes to Outputs:
  - cratedb = (sensitive value)

[...]

Destroy complete! Resources: 22 destroyed.
```

Terraform generates and deploys a self‑signed TLS certificate. After adding a
browser exception, CrateDB’s Admin UI prompts for HTTP Basic Auth. Authenticate
with the credentials shown above.

If authentication fails or no prompt appears:
- Wait a few minutes; provisioning can take time.
- Verify the load balancer is healthy and targets are in service.
- Confirm the security group allows inbound HTTPS from your IP.
- Ensure DNS/URL matches the ALB listener port (4200).

## Final Remarks

This Terraform configuration targets development or testing and is not
production‑ready (e.g., it does not configure high availability, disk encryption,
automated backups, or managed TLS certificates).
For production, consider using [CrateDB Cloud].

To request enhancements or share feedback, [open an issue on GitHub].


[CrateDB Cloud]: https://crate.io/products/cratedb-cloud/
[cratedb-terraform]: https://github.com/crate/cratedb-terraform
[open an issue on GitHub]: https://github.com/crate/cratedb-terraform/issues
[README]: https://github.com/crate/cratedb-terraform/blob/main/azure/README.md
[Terraform]: https://developer.hashicorp.com/terraform

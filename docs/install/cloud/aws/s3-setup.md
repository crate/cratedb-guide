```{highlight} yaml
```

(s3-setup)=

# Using Amazon S3 as a snapshot repository

CrateDB supports using the [Amazon S3] (Amazon Simple Storage Service) as a
snapshot repository. For this, you need to register the AWS plugin with
CrateDB.

## Basic configuration

Support for *Snapshot* and *Restore* to the [Amazon S3] service is enabled by
default in CrateDB. If you need to explicitly turn it off, disable the cloud
setting in the `crate.yml` file:

```
cloud.enabled: false
```

To be able to use the S3 API, CrateDB must [sign the requests] by using AWS
credentials consisting of an access key and a secret key. Therefore AWS
provides [IAM roles] to avoid any distribution of your AWS credentials to the
instances.

(s3-authentication)=

### Authentication

It is recommended to restrict the permissions of CrateDB on the S3 to only the
required extend. First, an IAM role is required. This [AWS guide] gives a
short description of how to create a policy offer using the CLI or the AWS
management console. Further, access of the snapshot to the S3 bucket needs to
be restricted. An example policy file granting anybody access to a bucket
called `snaps.example.com` is attached below:

```json
{
  "Statement": [
    {
      "Action": [
        "s3:ListBucket",
        "s3:GetBucketLocation",
        "s3:ListBucketMultipartUploads",
        "s3:ListBucketVersions"
      ],
      "Effect": "Allow",
      "Principal": "*",
      "Resource": [
        "arn:aws:s3:::snaps.example.com"
      ]
    },
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:AbortMultipartUpload",
        "s3:ListMultipartUploadParts"
      ],
      "Effect": "Allow",
      "Principal": "*",
      "Resource": [
        "arn:aws:s3:::snaps.example.com/*"
      ]
    }
  ],
  "Version": "2012-10-17"
}
```

Access permissions can be further restricted to a specific AWS Principal by
changing the `Statement.Principal` setting. Please refer to [AWS principals]
for more information.

For further AWS policy examples and detailed information, please refer to
[AWS policy examples] and the links therein.

It has to be noted, that the bucket needs to exist before registering a
repository for snapshots within CrateDB. CrateDB can also be allowed to create
the bucket. However this requires the following permissions to be contained
within the policy:

```json
{
   "Action": [
      "s3:CreateBucket"
   ],
   "Effect": "Allow",
   "Resource": [
      "arn:aws:s3:::snaps.example.com"
   ]
}
```

[amazon s3]: https://aws.amazon.com/s3/
[aws guide]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html
[aws policy examples]: https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html
[aws principals]: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html
[iam roles]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
[sign the requests]: https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html

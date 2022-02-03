Sample illustration of AWS EC2 Launch instance compatibility with OCI .
-------

Objective (Its for an internal demo)

----

- Launch an AWS EC2 CLI with LaunchInstance option and redirect the same to OCI and create a compute instance 


Setup

-----

- Setup an OCI function - https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm 
  - Use the code base here as func.py and func.yaml .
  - Update func.py with the regions values and config files with proper mapping.

- Setup an OCI  API gateway ,and create a deployment(as RunInstances) endpoint using the functions created above. - https://docs.oracle.com/en-us/iaas/Content/APIGateway/home.htm 

- Create an OCI IAM Customer secret key (which can be used as an aws auth with compatible endpoints) - https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#Working2



Execution from AWS Cloud shell 

----

```
aws configure (Update the AWS credentials as created via OCI )
```

```
aws ec2 run-instances --image-id ami-xxxx --count 1 --instance-type <VM Type from your shapeconfig file>  --subnet-id subnet-XXXX --endpoint-url https://xxxx.apigateway.<oci_region>.oci.customer-oci.com/v1/RunInstances  --output json --profile <AWS Profile>
```
Its Just for a demo purpose .





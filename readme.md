Sample illustration of AWS EC2  terminate  instance details wtih a  compatibility endpoint .
-------

Objective (Its for an internal demo)

----

- Terminate an incident from OCI using AWS CLI


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
aws ec2 describe-instances  --endpoint-url https://xxxx.apigateway.us-phoenix-1.oci.customer-oci.com/v2/TerminateInstances --output json --profile oci --instance-ids ocid1.instance.oc1.phx.xxxx
```
Its Just for a demo purpose .





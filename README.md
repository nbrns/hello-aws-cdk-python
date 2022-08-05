# Hello AWS CDK Python

Messing around with AWS CDK for Python to deploy an EKS (Managed k8s in AWS).

## Configure AWS Account

```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_DEFAULT_REGION=us-east-1
```

## Bootstrap And Deploy With CDK

```bash
cdk bootstrap
cdk synth
cdk deploy
```

## Connecting to the EKS cluster

As CDK uses the CloudFormation role to create the cluster, your default AWS user won't get access to the EKS cluster implicitly. Thus, you need to connect to the cluster by assuming the generated masters role.
You can easily identity it when scanning through your roles as it should look somewhat like <STACK_NAME>-<EKS_NAME>MastersRole<RANDOM_STUFF>.

```bash
 aws eks --region <REGION> update-kubeconfig --name <CLUSTER_NAME> --role-arn <EKS_MASTERS_ROLE_ARN>
 kubectl get namespaces
```
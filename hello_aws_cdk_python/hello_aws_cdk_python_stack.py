from aws_cdk import (
    Stack,
)
from constructs import Construct
import aws_cdk.aws_eks as eks


class HelloAwsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        cluster = eks.Cluster(self, "hello-eks", version=eks.KubernetesVersion.V1_21)

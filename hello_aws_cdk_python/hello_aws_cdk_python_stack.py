from aws_cdk import (
    Stack,
)
from constructs import Construct
import aws_cdk.aws_s3 as s3


class HelloAwsCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "TestS3Bucket", versioned=True)

import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_aws_cdk_python.hello_aws_cdk_python_stack import HelloAwsCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hello_aws_cdk_python/hello_aws_cdk_python_stack.py
# def test_sqs_queue_created():
#     app = core.App()
#     stack = HelloAwsCdkPythonStack(app, "hello-aws-cdk-python")
#     template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_aws_cdk_python.hello_aws_cdk_python_stack import HelloAwsCdkPythonStack


app = cdk.App()
HelloAwsCdkPythonStack(app, "HelloAwsCdkPythonStack")

app.synth()

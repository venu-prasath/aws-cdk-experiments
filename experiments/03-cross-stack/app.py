#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cross_stack.cross_stack_stack import CrossStackStack
from cross_stack.py_handler_stack import PyHandlerStack


app = cdk.App()
starter_stack = CrossStackStack(app, "CrossStackStack")

PyHandlerStack(app, "PyHandlerStack", bucket=starter_stack.get_my_bucket)

app.synth()

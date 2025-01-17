import aws_cdk as core
import aws_cdk.assertions as assertions

from python_impl.python_impl_stack import PythonImplStack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_impl/python_impl_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonImplStack(app, "python-impl")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

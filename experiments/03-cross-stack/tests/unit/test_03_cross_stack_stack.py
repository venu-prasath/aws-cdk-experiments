import aws_cdk as core
import aws_cdk.assertions as assertions

from 03_cross_stack.03_cross_stack_stack import 03CrossStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 03_cross_stack/03_cross_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 03CrossStackStack(app, "03-cross-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

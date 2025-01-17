import aws_cdk as core
import aws_cdk.assertions as assertions

from py_metrics.py_metrics_stack import PyMetricsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in py_metrics/py_metrics_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PyMetricsStack(app, "py-metrics")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

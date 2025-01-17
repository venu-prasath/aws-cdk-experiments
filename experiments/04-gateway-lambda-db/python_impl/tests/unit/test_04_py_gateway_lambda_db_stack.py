import aws_cdk as core
import aws_cdk.assertions as assertions

from 04_py_gateway_lambda_db.04_py_gateway_lambda_db_stack import 04PyGatewayLambdaDbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 04_py_gateway_lambda_db/04_py_gateway_lambda_db_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 04PyGatewayLambdaDbStack(app, "04-py-gateway-lambda-db")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

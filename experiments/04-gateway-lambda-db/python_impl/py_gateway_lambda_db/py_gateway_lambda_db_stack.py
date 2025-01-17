from aws_cdk import (
    Stack,
    aws_apigateway,
    aws_lambda
)
from constructs import Construct

class PyRestApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        employee_lambda = aws_lambda.Function(
            self,
            "EmployeeLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=aws_lambda.Code.from_asset("services")
        )

        api = aws_apigateway.RestApi(self, "Py-Employee-Api")
        employee_resource = api.root.add_resource("empl")

        employee_lambda_integration = aws_apigateway.LambdaIntegration(employee_lambda)
        employee_resource.add_method("GET", employee_lambda_integration)
        employee_resource.add_method("POST", employee_lambda_integration)

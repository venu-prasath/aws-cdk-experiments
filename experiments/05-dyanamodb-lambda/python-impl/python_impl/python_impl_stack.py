from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_dynamodb as ddb
)
from constructs import Construct

class PythonImplStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        employee_table = ddb.TableV2(
            self,
            "EmployeeTablePy",
            partition_key=ddb.Attribute(
                name="id",
                type=ddb.AttributeType.STRING
            ),
            billing=ddb.Billing.on_demand(),
        )

        empl_lambda = _lambda.Function(
            self,
            "EmployeeLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=_lambda.Code.from_asset("services"),
            environment={
                "TABLE_NAME": employee_table.table_name
            }
        )

        employee_table.grant_read_write_data(empl_lambda)

        api = apigw.RestApi(self, "Py-Empl-Api")
        empl_resource = api.root.add_resource("empl")

        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)
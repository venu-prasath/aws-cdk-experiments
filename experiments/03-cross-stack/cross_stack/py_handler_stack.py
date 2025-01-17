from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda
)
from constructs import Construct

class PyHandlerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, bucket: s3.Bucket, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(self, "PythonLambda",
                            runtime=aws_lambda.Runtime.PYTHON_3_11,
                            code=aws_lambda.Code.from_inline(
                                "import os\ndef handler(event, context):\n print(os.environ['BUCKET_ARN'])"),
                            handler="index.handler",
                            environment={
                                "BUCKET_ARN": bucket.bucket_arn
                            },
                        )

        
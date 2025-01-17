from aws_cdk import (
    Stack,
    aws_s3 as s3,
    Duration,
    CfnOutput,
    Fn
)
from constructs import Construct

class PyStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        suffix = self._initialze_suffix()

        bucket = s3.Bucket(self, "PyDynamicBucket",
                           bucket_name = f"new-bucket-{suffix}", 
                           lifecycle_rules=[
            s3.LifecycleRule(
                expiration=Duration.days(3),
            )
        ])

        print("Bucket name: ", bucket.bucket_name)

        CfnOutput(self, "BucketName", value=bucket.bucket_name)

    def _initialze_suffix(self):
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        suffix = Fn.select(4, Fn.split('-', short_stack_id))
        return suffix
        

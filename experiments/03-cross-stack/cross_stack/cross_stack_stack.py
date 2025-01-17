from aws_cdk import (
    Stack,
    aws_s3 as s3,
    Duration,
    CfnOutput,
    Fn
)
from constructs import Construct

class CrossStackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        suffix = self._initialize_suffix()

        self.bucket = s3.Bucket(self, "CrossStackBucket",
                           bucket_name = f"new-bucket-{suffix}", 
                           lifecycle_rules=[
            s3.LifecycleRule(
                expiration=Duration.days(3),
            )
        ])


        CfnOutput(self, "BucketName", value=self.bucket.bucket_name)
    


    def _initialize_suffix(self):
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        suffix = Fn.select(4, Fn.split('-', short_stack_id))
        return suffix
    
    @property
    def get_my_bucket(self):
        return self.bucket
        

### CDK Intermediate Topics

##### 1. CDK IDs

Resources managed by CDK have 3 IDs:

1. Construct ID: The ID we provide ourselves. (eg. bucket = s3.Bucket(self, "my_construct_id"))
2. Logical ID: Construct ID + suffix from CDK used by Cloud Formation
   (Eg. Id generated in the template on compilation of CDK code)
3. Physical ID: Resource names. Used for reference inside other services (ARN)

Cloud Formation tracks resources by the generated logical Ids. If the Construct Id is changed in the code, on compilation, CDK generates new logical IDs for the resource. This will remove old resource and create new resource. The two potential problems of this

1. Accidental deletion of stateful resources - (s3, DynamoDB, RDS)
2. Resource already exists error

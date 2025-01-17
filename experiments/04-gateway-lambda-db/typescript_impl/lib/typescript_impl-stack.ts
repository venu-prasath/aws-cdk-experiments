import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { join } from "path";

export class TsRestApiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const employeeLambda = new NodejsFunction(this, "EmployeeLambda", {
      runtime: Runtime.NODEJS_18_X,
      handler: "handler",
      entry: join(__dirname, "..", "services", "handler.ts"),
    });

    const api = new cdk.aws_apigateway.RestApi(this, "Ts-Empl-Api");
    const emplResource = api.root.addResource("empl");

    const emplLambdaIntegration = new cdk.aws_apigateway.LambdaIntegration(
      employeeLambda
    );
    emplResource.addMethod("GET", emplLambdaIntegration);
    emplResource.addMethod("POST", emplLambdaIntegration);
  }
}

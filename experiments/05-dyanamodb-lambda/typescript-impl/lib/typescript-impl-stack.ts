import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { join } from "path";
import {
  Cors,
  LambdaIntegration,
  ResourceOptions,
  RestApi,
} from "aws-cdk-lib/aws-apigateway";
import { AttributeType, Billing, TableV2 } from "aws-cdk-lib/aws-dynamodb";

export class TypescriptImplStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const emplTable = new TableV2(this, "TsEmplTable", {
      partitionKey: { name: "id", type: AttributeType.STRING },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      billing: Billing.onDemand(),
    });

    const employeeLambda = new NodejsFunction(this, "EmployeeLambda", {
      runtime: Runtime.NODEJS_18_X,
      handler: "handler",
      entry: join(__dirname, "..", "services", "handler.ts"),
      environment: {
        TABLE_NAME: emplTable.tableName,
      },
    });

    emplTable.grantReadWriteData(employeeLambda);

    const api = new RestApi(this, "EmployeeApi");

    const optionsWithCors: ResourceOptions = {
      defaultCorsPreflightOptions: {
        allowOrigins: Cors.ALL_ORIGINS,
        allowMethods: Cors.ALL_METHODS,
      },
    };

    const emplResource = api.root.addResource("empl", optionsWithCors);

    const emplLambdaIntegration = new LambdaIntegration(employeeLambda);
    emplResource.addMethod("GET", emplLambdaIntegration);
    emplResource.addMethod("POST", emplLambdaIntegration);
  }
}

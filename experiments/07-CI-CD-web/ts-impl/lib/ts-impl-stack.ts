import * as cdk from "aws-cdk-lib";
import { Distribution, OriginAccessIdentity } from "aws-cdk-lib/aws-cloudfront";
import { S3Origin } from "aws-cdk-lib/aws-cloudfront-origins";
import { Bucket } from "aws-cdk-lib/aws-s3";
import { BucketDeployment } from "aws-cdk-lib/aws-s3-deployment";
import { Construct } from "constructs";
import { join } from "path";
import { Source } from "aws-cdk-lib/aws-s3-deployment";

export class TsImplStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const deploymentBucket = new Bucket(this, "DeploymentBucket");

    const uiDir = join(__dirname, "..", "..", "webapp", "dist");
    if (!uiDir) {
      console.warn("Dist directory not found. Skipping deployment of UI");
      return;
    }

    const originAccessIdentity = new OriginAccessIdentity(
      this,
      "OriginAccessIdentity"
    );
    deploymentBucket.grantRead(originAccessIdentity);

    const distribution = new Distribution(this, "WEbDistribution", {
      defaultRootObject: "index.html",
      defaultBehavior: {
        origin: new S3Origin(deploymentBucket, {
          originAccessIdentity: originAccessIdentity,
        }),
      },
    });

    new BucketDeployment(this, "WebDeployment", {
      sources: [Source.asset(uiDir)],
      destinationBucket: deploymentBucket,
      distribution: distribution,
    });
  }
}

import * as cdk from "aws-cdk-lib";
import { Alarm, Metric } from "aws-cdk-lib/aws-cloudwatch";
import { SnsAction } from "aws-cdk-lib/aws-cloudwatch-actions";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Topic } from "aws-cdk-lib/aws-sns";
import { LambdaSubscription } from "aws-cdk-lib/aws-sns-subscriptions";
import { Construct } from "constructs";
import { join } from "path";

export class TsMetricsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const webHookLambda = new NodejsFunction(this, "webHookLambda", {
      runtime: Runtime.NODEJS_18_X,
      handler: "handler",
      entry: join(__dirname, "..", "services", "hook.ts"),
    });

    const alarmTopic = new Topic(this, "TSAlarmTopic", {
      displayName: "TSAlarmTopic",
      topicName: "TSAlarmTopic",
    });

    alarmTopic.addSubscription(new LambdaSubscription(webHookLambda));

    const alarm = new Alarm(this, "TSAlarm", {
      metric: new Metric({
        metricName: "TSAlarmMetric",
        namespace: "Custom",
        period: cdk.Duration.minutes(1),
        statistic: "Sum",
      }),
      evaluationPeriods: 1,
      threshold: 1,
    });

    const topicAction = new SnsAction(alarmTopic);
    alarm.addAlarmAction(topicAction);
    alarm.addOkAction(topicAction);
  }
}

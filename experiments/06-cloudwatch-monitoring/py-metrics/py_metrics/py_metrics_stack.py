from aws_cdk import (
    Stack,
    aws_lambda,
    aws_sns,
    aws_sns_subscriptions,
    Duration,
    aws_cloudwatch,
    aws_cloudwatch_actions
)
from constructs import Construct

class PyMetricsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        web_hook_lambda = aws_lambda.Function(
            self,
            "webhookLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            code=aws_lambda.Code.from_asset("services"),
            handler="hook.handler",
        )

        alarm_topic = aws_sns.Topic(
            self,
            "pyAlarmTopic",
            display_name="PyAlarmTopic", 
            topic_name="PyAlarmTopic"
        ) 

        alarm_topic.add_subscription(
            aws_sns_subscriptions.LambdaSubscription(web_hook_lambda)
        )

        alarm = aws_cloudwatch.Alarm(
            self,
            "ApiAlarm",
            metric=aws_cloudwatch.Metric(
                metric_name="custom_metric",
                namespace="Custom",
                period=Duration.minutes(1),
                statistic="Sum",
            ),
            evaluation_periods=1,
            threshold=100,
        )

        topic_action = aws_cloudwatch_actions.SnsAction(alarm_topic)
        alarm.add_alarm_action(topic_action)
        alarm.add_ok_action(topic_action)

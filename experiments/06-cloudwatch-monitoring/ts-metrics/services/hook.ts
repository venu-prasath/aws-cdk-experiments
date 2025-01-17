import { SNSEvent } from "aws-lambda";

const webHookUrl =
  "https://hooks.slack.com/services/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";

async function handler(event: SNSEvent) {
  for (const record of event.Records) {
    await fetch(webHookUrl, {
      method: "POST",
      body: JSON.stringify({
        text: `SNS Message: ${record.Sns.Message}`,
      }),
    });
  }
}

export { handler };

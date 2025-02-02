import urllib3
import json

http = urllib3.PoolManager()

def handler(event, context):
    print("Calling Slack webhook")
    url = "https://hooks.slack.com/services/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"
    msg = {
        "channel": "#aws-events",
        "text": event['Records'][0]['Sns']['Message']
    }

    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'],
        "status_code": resp.status,
        "response": resp.data
    })
import {
  DynamoDBClient,
  GetItemCommand,
  ScanCommand,
} from "@aws-sdk/client-dynamodb";
import { unmarshall } from "@aws-sdk/util-dynamodb";
import {
  APIGatewayProxyEvent,
  APIGatewayProxyResult,
  Context,
} from "aws-lambda";

const client = new DynamoDBClient({ region: "us-east-1" });

export async function getEmpl(
  event: APIGatewayProxyEvent,
  ddbClient: DynamoDBClient
): Promise<APIGatewayProxyResult> {
  if (event.queryStringParameters && "id" in event.queryStringParameters) {
    const id = event.queryStringParameters["id"]!;
    const getItemResponse = await client.send(
      new GetItemCommand({
        TableName: process.env.TABLE_NAME,
        Key: {
          id: { S: id },
        },
      })
    );
    if (getItemResponse.Item) {
      const unmarsalledItem = unmarshall(getItemResponse.Item);
      return {
        statusCode: 200,
        body: JSON.stringify(unmarsalledItem),
      };
    }
  }
  return {
    statusCode: 400,
    body: JSON.stringify("Bad Request"),
  };
}

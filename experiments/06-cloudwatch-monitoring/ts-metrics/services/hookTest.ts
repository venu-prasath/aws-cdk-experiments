import { handler } from "./hook";

handler({
  Records: [
    {
      Sns: {
        Message: "SNS Message test from Typescript",
      },
    },
  ],
} as any);

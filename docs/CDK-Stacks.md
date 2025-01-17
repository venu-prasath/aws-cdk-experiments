# Organizing AWS CDK Stacks

When working with AWS Cloud Development Kit (CDK), organizing your stacks effectively ensures scalability, maintainability, and easier collaboration. This guide outlines best practices and considerations for structuring your CDK application.

---

## 1. **Understand CDK Concepts**

Before diving into organization strategies, ensure you’re familiar with the key concepts of CDK:

- **App**: The root of your CDK application, which synthesizes to a CloudFormation template.
- **Stack**: Represents a single CloudFormation stack.
- **Construct**: Basic building blocks of CDK apps, encapsulating AWS resources.

---

## 2. **Folder and File Structure**

A well-organized folder structure makes your project easy to navigate. Here’s a suggested structure:

```
project-root/
├── bin/
│   └── app.ts (or app.py, app.js, etc.)
├── lib/
│   ├── network-stack.ts
│   ├── compute-stack.ts
│   ├── database-stack.ts
│   └── constructs/
│       ├── vpc-construct.ts
│       ├── ecs-cluster-construct.ts
│       └── s3-bucket-construct.ts
├── test/
│   └── test-network-stack.ts
├── cdk.json
├── package.json (or equivalent for your language)
└── README.md
```

### Explanation

- **bin/**: Contains the entry point for your CDK app. This is where you instantiate stacks.
- **lib/**: Houses the stacks and reusable constructs. Group related resources into separate stacks and abstract repetitive patterns into constructs.
- **test/**: Contains unit and integration tests for your stacks and constructs.

---

## 3. **Stack Design Principles**

### a. Group Resources by Lifecycle

Organize resources into stacks based on their lifecycle. For example:

- **Networking Stack**: VPC, subnets, security groups.
- **Compute Stack**: ECS, Lambda functions, or EC2 instances.
- **Database Stack**: RDS, DynamoDB tables.

### b. Limit Stack Size

Avoid creating monolithic stacks with too many resources. This makes deployment faster and troubleshooting easier.

### c. Use Cross-Stack References

Use exports and imports to share resources between stacks while maintaining separation of concerns. Example:

```typescript
// In NetworkStack
export class NetworkStack extends Stack {
  public readonly vpc: ec2.Vpc;

  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    this.vpc = new ec2.Vpc(this, "VPC", {
      maxAzs: 3,
    });
  }
}

// In ComputeStack
import { NetworkStack } from "./network-stack";

export class ComputeStack extends Stack {
  constructor(
    scope: Construct,
    id: string,
    networkStack: NetworkStack,
    props?: StackProps
  ) {
    super(scope, id, props);

    new ecs.Cluster(this, "Cluster", {
      vpc: networkStack.vpc,
    });
  }
}
```

---

## 4. **Use Constructs for Reusability**

Encapsulate complex logic and repetitive resource patterns into constructs. This makes your code more modular and reusable.

Example:

```typescript
import { Construct } from "constructs";
import * as s3 from "aws-cdk-lib/aws-s3";

export class S3BucketConstruct extends Construct {
  public readonly bucket: s3.Bucket;

  constructor(scope: Construct, id: string, props?: s3.BucketProps) {
    super(scope, id);

    this.bucket = new s3.Bucket(this, "Bucket", props);
  }
}
```

---

## 5. **Environment-Specific Stacks**

Use environment variables or context to deploy stacks to different environments (e.g., dev, staging, production).

### Example:

```typescript
const envDev = { account: "111111111111", region: "us-east-1" };
const envProd = { account: "222222222222", region: "us-west-1" };

new NetworkStack(app, "NetworkStack-Dev", { env: envDev });
new NetworkStack(app, "NetworkStack-Prod", { env: envProd });
```

---

## 6. **Testing Stacks**

Use the CDK assertions library to write unit tests for your stacks.

Example:

```typescript
import * as cdk from "aws-cdk-lib";
import { Template } from "aws-cdk-lib/assertions";
import { NetworkStack } from "../lib/network-stack";

test("VPC Created", () => {
  const app = new cdk.App();
  const stack = new NetworkStack(app, "TestStack");
  const template = Template.fromStack(stack);

  template.hasResourceProperties("AWS::EC2::VPC", {
    CidrBlock: "10.0.0.0/16",
  });
});
```

---

## 7. **Best Practices Summary**

- Follow the **single responsibility principle** for stacks.
- Abstract common logic into reusable constructs.
- Avoid hardcoding values; use context or environment variables.
- Test your stacks and constructs rigorously.
- Document the purpose and dependencies of each stack.

By adopting these organizational practices, your AWS CDK projects will remain manageable, scalable, and easy to collaborate on as your infrastructure grows.

---

## References

- [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [CDK Patterns](https://cdkpatterns.com/)

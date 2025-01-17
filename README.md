# CDK Experiments

This repository contains various experiments and starter projects for AWS Cloud Development Kit (CDK) using different languages and setups.

## Project Structure

.gitignore
README.md
docs/
experiments/
01-py-starter/
02-ts-starter/
03-cross-stack/
04-gateway-lambda-db/
05-dyanamodb-lambda/
06-cloudwatch-monitoring/
07-CI-CD-web/
s3template.json

## Experiments

### 01-py-starter

A starter project for CDK development with Python.

### 02-ts-starter

A starter project for CDK development with TypeScript.

### 03-cross-stack

An experiment demonstrating cross-stack references in CDK using Python.

### 04-gateway-lambda-db

An experiment demonstrating API Gateway, Lambda, and DynamoDB integration using TypeScript and Python.

### 05-dyanamodb-lambda

An experiment demonstrating DynamoDB and Lambda integration using TypeScript.

### 06-cloudwatch-monitoring

An experiment demonstrating CloudWatch monitoring using TypeScript and Python.

### 07-CI-CD-web

An experiment demonstrating CI/CD for a web application using TypeScript and Python.

## Useful Commands

### For TypeScript Projects

- `npm run build` - Compile TypeScript to JavaScript
- `npm run watch` - Watch for changes and compile
- `npm run test` - Perform the Jest unit tests
- `npx cdk deploy` - Deploy this stack to your default AWS account/region
- `npx cdk diff` - Compare deployed stack with current state
- `npx cdk synth` - Emit the synthesized CloudFormation template

### For Python Projects

- `cdk ls` - List all stacks in the app
- `cdk synth` - Emit the synthesized CloudFormation template
- `cdk deploy` - Deploy this stack to your default AWS account/region
- `cdk diff` - Compare deployed stack with current state
- `cdk docs` - Open CDK documentation

## Documentation

Refer to the [docs](docs) directory for detailed guides and best practices:

- [CDK-Constructs](docs/CDK-Constructs)
- [CDK-Intermediate.md](docs/CDK-Intermediate.md)
- [CDK-Stacks.md](docs/CDK-Stacks.md)

## License

This project is licensed under the MIT license.

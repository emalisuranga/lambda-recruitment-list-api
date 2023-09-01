# AWS Lambda Function for Recruitment List

This AWS Lambda function serves as an essential component for managing and retrieving recruitment data efficiently. It integrates seamlessly with Amazon DynamoDB and provides a RESTful API for accessing and updating recruitment records.

## Functionality

The Lambda function offers the following key functionality:

- **Query by ID and Status:** It can retrieve recruitment records based on the provided `cn_id` (candidate ID) and `status` parameters.

- **Error Handling:** The function is equipped with error handling to ensure smooth execution, even in the face of unexpected issues.

- **CORS Support:** CORS (Cross-Origin Resource Sharing) headers are included to allow integration with web applications from different domains.

## Usage

To use this Lambda function, you can invoke it using the AWS Lambda service, or you can deploy it as part of a larger application.

### Invoking the Function

To invoke the function, make an HTTP GET request to its endpoint, passing the `cn_id` and `status` as query parameters. The function will respond with the requested data or an appropriate error message.

Example Request:
GET /recruitment?cn_id=123&status=active


### Deployment

If you wish to deploy this Lambda function for your project, you can follow these steps:

1. Clone this repository to your local development environment.

2. Set up an AWS Lambda function and associate it with the code from this repository.

3. Configure the necessary permissions and environment variables for your Lambda function, including the DynamoDB table name.

4. Deploy the Lambda function.

5. Ensure that CORS settings are adjusted to match your project's requirements.

## Configuration

You can customize this Lambda function by modifying its configuration to suit your specific needs. Ensure that you set appropriate CORS headers, error handling, and access control based on your application's requirements.

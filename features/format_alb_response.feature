Feature: Format an ALB response for Python Serverless Functions in AWS Lambda

    Scenario: Format an ALB response for Python Serverless Functions in AWS Lambda
        Given a response in json format
        When a call to alb_response is made
        Then the format should be correct for the AWS ALB response

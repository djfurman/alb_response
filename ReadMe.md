[![](https://img.shields.io/pypi/l/Django.svg?style=plastic)](./LICENSE.md)
![Code Style - Black](https://raw.githubusercontent.com/ambv/black/master/docs/_static/logo2-readme.png)

# AWS ALB Response Creator

The AWS announcement of [Application Load Balancers supporting Lambda functions](https://aws.amazon.com/blogs/networking-and-content-delivery/lambda-functions-as-targets-for-application-load-balancers/) made my reInvent experience!

## Purpose

In doing a PoC however, I found that the `statusDescription` element was somewhat of an annoyance to code. This package provides a method to return the appropriate format of this field without copy/paste response data and allowing a strategy to implement this to swap out response formats for API Gateway or ALB as needed.

## Installation

Run `pip install alb-response`

## Usage

```python
from alb_response import alb_response

def lambda_handler(event, context):

    response_dict = process_the_event(event)

    return alb_response(
        http_status=200,
        json=response_dict,
        is_base64_encoded=False,
    )
```

### Architecture

1. Setup an Application Load Balancer (ALB)
1. Create a target group for the Lambda
1. Assign appropriate permissions to your Lambda function
1. Attach the target group to the ALB with a rule

[![License](https://img.shields.io/pypi/l/Django.svg?style=plastic)](./LICENSE.md)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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

## Contributing

Contributions are welcome! Please open an issue or make a pull request.

If making a pull request, please run the tests and ensure that you maintain or increase code coverage.

### Dependencies

To make this project more portable and keep environments organized, this project leverages `pipenv`. To install deterministic dependencies, run `pipenv sync`.

### Run Tests

To run the tests, install the dependencies and run `behave`.

To get code coverage as well, run `coverage run --source='.' -m behave` followed by `coverage report`.

# Release Log

- `0.1.0`
  - Initial Release
- `0.1.1`
  - Dependency update to resolve [CVE-2019-11324](https://nvd.nist.gov/vuln/detail/CVE-2019-11324).

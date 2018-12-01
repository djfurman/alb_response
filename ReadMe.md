# AWS ALB Response Creator

The AWS announcement of [Application Load Balancers supporting Lambda functions](https://aws.amazon.com/blogs/networking-and-content-delivery/lambda-functions-as-targets-for-application-load-balancers/) made my reInvent experience!

## Purpose 

In doing a PoC however, I found that the `statusDescription` element was somewhat of an annoyance to code. This package provides a method to return the appropriate format of this field

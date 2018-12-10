from behave import given, when, then
from alb_response import alb_response


@given(u"a response in json format")
def setup_a_json_format_response(context):
    context.is_json_response = True
    context.data_payload = None
    context.json_payload = {"key1": "value1", "key2": "value2"}
    context.response_arguments = {
        "http_status": 200,
        "is_base64_encoded": False,
        "headers": None,
    }


@when(u"a call to alb_response is made")
def call_the_alb_response(context):
    context.alb_response = alb_response(
        http_status=context.response_arguments["http_status"],
        data=context.data_payload,
        json=context.json_payload,
        headers=context.response_arguments["headers"],
        is_base64_encoded=context.response_arguments["is_base64_encoded"],
    )


@then(u"the format should be correct for the AWS ALB response")
def assert_the_response_contains_elements(context):
    assert int(context.alb_response["statusCode"]) is not None
    assert int(context.alb_response["statusCode"]) == int(
        context.response_arguments["http_status"]
    )
    assert context.alb_response["isBase64Encoded"] is not None
    assert isinstance(context.alb_response["isBase64Encoded"], bool)
    assert context.alb_response["headers"] is not None
    assert isinstance(context.alb_response["headers"], dict)

import json as py_json
from http import HTTPStatus


def alb_response(
    http_status, data=None, json=None, headers=None, is_base64_encoded=False
):

    response_headers = {}
    status_code = HTTPStatus(http_status)

    status_description = build_status_description(int(status_code))

    if json:
        response_headers["content-type"] = "application/json"
        if headers is not None:
            response_headers.update(headers)
        if isinstance(json, str):
            payload = json
        else:
            payload = py_json.dumps(json)
    else:
        payload = data

        if headers is None:
            response_headers["content-type"] = "text/plain"
        else:
            response_headers.update(headers)

    response = {
        "isBase64Encoded": is_base64_encoded,
        "statusCode": int(http_status),
        "statusDescription": status_description,
        "headers": response_headers
    }
    if payload:
        response["body"] = payload
        
    return response



def build_status_description(status_code):
    """Creates the strange format of status description required by the AWS ALB feature for serverless applications

    Arguments:
        status_code {int} -- http status code

    Returns:
        str -- AWS ALB compliant status description
    """

    status = HTTPStatus(status_code)
    return f"{int(status)} {str(status).split('.')[1].replace('_', ' ')}"

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print(response)
    if response is not None:
        try:
            message = response.data["detail"]
            print(message)
            response.data["status_code"] = response.status_code
            response.data["detail"] = message
        except KeyError:
            print(response.data)
    return response

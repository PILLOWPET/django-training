from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        try:
            message = response.data["detail"]
            response.data["status_code"] = response.status_code
            response.data["detail"] = message
        except KeyError:
            pass
    return response

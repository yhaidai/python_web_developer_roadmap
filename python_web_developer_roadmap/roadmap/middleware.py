from pprint import pprint


def logging_middleware(get_response):
    def middleware(request):
        pprint(dict(request.headers))
        response = get_response(request)
        return response

    return middleware

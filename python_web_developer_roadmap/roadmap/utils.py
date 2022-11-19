import requests


def get_request(request, *args, **kwargs):
    headers = kwargs.setdefault("headers", {})
    headers["Cookie"] = headers.get("Cookie", request.headers["Cookie"])
    return requests.get(*args, **kwargs)

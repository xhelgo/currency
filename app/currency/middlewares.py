from time import time

from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        total_time = time() - start

        RequestResponseLog.objects.create(path=request.path, request=request.method, time=total_time)

        return response

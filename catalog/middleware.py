from catalog.models import LogModel


# Middleware for logging all requests except requests to admin part.
class LogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith('/admin'):
            path = request.path_info
            method = request.method
            log = LogModel(path=path, method=method)
            log.save()
        return self.get_response(request)

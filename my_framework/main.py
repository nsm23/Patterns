from views import PageNotFound


class Framework:

    def __init__(self, routes_obj, fronts_obj):
        self.routes = routes_obj
        self.fronts = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        request = {}
        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound()

        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


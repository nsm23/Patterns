from quopri import decodestring
from views import PageNotFound
from my_framework.requests import PostRqst, GetRqst


class Framework:
    def __init__(self, routes_obj, fronts_obj):
        self.routes = routes_obj
        self.fronts = fronts_obj

    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]
        request = {}
        if not path.endswith("/"):
            path = f"{path}/"

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound()

        method = environ["REQUEST_METHOD"]
        request["method"] = method

        if method == "GET":
            request_param = GetRqst().get_param(environ)
            request["request_param"] = request_param
            print(f"get params - {request_param}")
        if method == "POST":
            data = PostRqst().request_param(environ)
            request["data"] = data
            print(f"post request: {Framework.decod_func(data)}")

        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]

    @staticmethod
    def decod_func(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'utf-8')
            val_decode_str = decodestring(val).decode('utf-8')
            new_data[k] = val_decode_str
        return new_data

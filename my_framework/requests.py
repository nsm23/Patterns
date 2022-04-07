class InputData:
    @staticmethod
    def parse_data(data: str):
        result = {}
        if data:
            addr = data.split("&")
            for i in addr:
                k, v = i.split("=")
                result[k] = v
        return result


class GetRqst:
    @staticmethod
    def get_param(environ):
        query_str = environ["QUERY_STRING"]
        rqst_param = InputData.parse_data(query_str)
        return rqst_param


class PostRqst:
    @staticmethod
    def input_data(env) -> bytes:
        length_data = env.get("CONTENT_LENGTH")
        content_data = int(length_data) if length_data else 0
        if content_data > 0:
            data = env["wsgi.input"].read(content_data)
        else:
            data = b""
        return data

    def parse_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding="utf-8")
            result = InputData.parse_data(data_str)
        return result

    def request_param(self, environ):
        data = self.input_data(environ)
        data = self.parse_input_data(data)
        return data

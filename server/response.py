class Response:

    def __init__(self, body, err):
        self.result = body
        self.result_type = type(body)
        self.error = str(err)
import json

class Response:

    def __init__(self, res, err):
        self.result = res
        self.result_type = type(res).__name__
        self.error = str(err)

    def to_json(self):
        return json.dumps(self.__dict__)

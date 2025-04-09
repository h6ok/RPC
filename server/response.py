import json

class Response:

    def __init__(self, body, err):
        self.result = body
        self.error = str(err)

    def to_json(self):
        return json.dumps(self.__dict__)

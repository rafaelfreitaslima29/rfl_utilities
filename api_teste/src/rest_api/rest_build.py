


class RestBuilder:


    def __init__(self, endpoint: str) -> None:
        self.METHOD_GET = "GET"
        self.METHOD_POST = "POST"
        
        self.endpoint = endpoint
        self.http_method = self.METHOD_GET



    def m_method(self, http_method: str):
        self.http_method = http_method
        return self



    def m_to_string(self):
        configs = f"""
        ENDPOINT = {self.endpoint}
        METHOD   = {self.http_method}
        """
        print(configs) 
import requests
import json
import pandas as pd


class RestBuilder:


    def __init__(self, domain: str) -> None:
        self.METHOD_GET     = "GET"
        self.METHOD_POST    = "POST"
        self.METHOD_HEAD    = "HEAD"
        self.METHOD_PUT     = "PUT"
        self.METHOD_DELETE  = "DELETE"
        self.METHOD_PATCH   = "PATCH"
        self.METHOD_CONNECT = "CONNECT"
        self.METHOD_TRACE   = "TRACE"
        self.METHOD_OPTIONS = "OPTIONS"
        
        self.domain      = domain
        self.endpoint    = ""
        self.port        = ""
        self.http_method = self.METHOD_GET
        self.headers     = None
        self.body        = None 
        self.file        = None
        self.debug       = False



    def m_set_method(self, http_method: str):
        self.http_method = http_method
        return self



    def m_set_port(self, port: str):
        self.port = port
        return self



    def m_set_endpoint(self, endpoint: str):
        self.endpoint = endpoint
        return self



    def m_set_headers(self, headers_dict: dict):
        self.headers = headers_dict
        return self



    def m_set_body(self, body_dict: dict):
        self.body = body_dict
        return self



    def m_set_file(self, file):
        self.file = file
        return self



    def m_debug_on(self):
        self.debug = True
        return self


    def m_to_string(self):
        configs = f"""
        DOMAIN   = {self.domain}
        PORT     = {self.port}
        ENDPOINT = {self.endpoint}
        METHOD   = {self.http_method}
        HEADERS  = {self.headers}
        BODY     = {self.body}
        URL  = {self.http_method} -> {self.mp_url_build()}
        """
        print(configs)



    def m_send_request(self):
        print("GET     - IMPLEMENTAÇÃO INCOMPLETA")
        print("POST    - IMPLEMENTAÇÃO TESTE")
        print("HEAD    - SEM IMPLEMENTAÇÃO")
        print("PUT     - SEM IMPLEMENTAÇÃO")
        print("DELETE  - SEM IMPLEMENTAÇÃO")
        print("PATCH   - SEM IMPLEMENTAÇÃO")
        print("CONNECT - SEM IMPLEMENTAÇÃO")
        print("TRACE   - SEM IMPLEMENTAÇÃO")
        print("OPTIONS - SEM IMPLEMENTAÇÃO")

        if self.http_method == self.METHOD_GET: 
            return self.mp_get_request()
        
        if self.http_method == self.METHOD_POST: 
            return self.mp_post_request()



    def mp_post_request(self):
        if self.http_method == self.METHOD_POST:
            req = requests.post(url= self.mp_url_build(), data=json.dumps(self.body), files=self.file, headers= self.headers )

            print( req.status_code )

            if self.debug == True:
                print("Debug False")
                return req.text
            
            if self.debug == False:
                print("Debug False")
                return req.json()





    def mp_get_request(self):
        
        if self.http_method == self.METHOD_GET:
            req = requests.get(url= self.mp_url_build(), headers= self.headers )

            print( req.status_code )

            if self.debug == True:
                return req.json()
            
            if self.debug == False:
                return req.json()
        



    def mp_url_build(self):
        url = ""
        
        # REMOVENDO ESPAÇOS NO INÍCIO E FINAL
        self.port     = self.port.strip()
        self.domain   = self.domain.strip()
        self.endpoint = self.endpoint.strip()

        # SE A PORTA FOR DIFERENTE DA "", PORTA PADRÃO 80
        if self.port != "":
            
            # SE O DOMINIO TERMINA COM "/""
            if self.domain[-1] == "/":
                # RETIRA A BARRA NO FINAL
                self.domain = self.domain[:-1]
                # 
                url = f'{self.domain + ":" + self.port + "/"+ self.endpoint}'
                # print(self.domain)
                # print(url)
                return url
            
            # SE O DOMINIO TERMINA NÃO COM "/""
            if self.domain[-1] != "/":
                url = f'{self.domain + ":" + self.port + "/"+ self.endpoint}'
                # print(self.domain)
                # print(url)
                return url
            
        # SE USA A PORTA PADRÃO
        if self.port == "" or self.port == "80":
            # SE VIER A PORTA 80 DEIXA ELA EM BRANCO
            self.port = ""

            # SEM BARRA O FINAL DO DOMÍNIO
            if self.domain[-1] != "/":
                # ADICIONAR A BARRA NO FINAL
                self.domain = self.domain + "/"
                url = f'{self.domain + self.endpoint}'
                return url
            
            # COM BARRA O FINAL DO DOMÍNIO
            if self.domain[-1] == "/":
                # ADICIONAR O ENDPOINT
                url = f'{self.domain + self.endpoint}'
                return url
            

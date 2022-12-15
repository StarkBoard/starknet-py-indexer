import json
import requests

class Provider:
    """RPCProvider module

    Parameter
    --------
    provider_url: str
        jsonRPC Provider URL
    """
    def __init__(self, provider_url, **kwargs):
        self.provider_url = provider_url
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])
        self.base_request_data = {"jsonrpc":"2.0", "id":1, "method":"", "params":[]}
        
    def _get_request_data(self, method, params):
        request_data = self.base_request_data
        request_data["method"] = method
        request_data["params"] = params
        return json.dumps(request_data)

    def get(self, url, **kwargs):
        return self.session.get(self.provider_url+url, **kwargs)

    def post(self, method="", params=[], **kwargs):
        data = self._get_request_data(method, params)
        return self.session.post(self.provider_url, data=data, **kwargs)

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                Provider.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination

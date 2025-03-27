"""Endpoints module for package pytechnitiumapi."""

class BeerListEndpoint(RequestsEndpoint):
    method = Methods.GET
    url = "https://random-data-api.com/api/v2/beers"
    params = {"response_type": "json"}
    models = {"response": NamedTupleParser(model=Beer, many=True)}

    def __init__(self, size):
        self.params["size"] = size

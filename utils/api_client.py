import requests


class APIClient:
    def get(self, url):
        return requests.get(url)

    def post(self, url, json_body):
        return requests.post(url, json=json_body)

    def put(self, url, json_body):
        return requests.put(url, json=json_body)

    def delete(self, url):
        return requests.delete(url)
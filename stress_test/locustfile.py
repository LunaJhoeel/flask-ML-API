from dataclasses import dataclass
from email import header
from locust import HttpUser, task, between


class APIUser(HttpUser):
    wait_time = between(1,5)
    @task(1)
    def index(self):
        self.client.get("http://0.0.0.0/")

    @task(4)
    def predict(self):
        files = [('file',('dog.jpeg',open('dog.jpeg','rb'), "image/jpeg"))]
        headers = {}
        payload = {}
        self.client.post("http://0.0.0.0/predict",
            headers = headers,
            data = payload,
            files = files
            )
    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.

import requests
import time

class Smsnator:
    def __init__(self):
        self.session = requests.Session()
        self.session.get("https://smsnator.online/")
        self.headers = {
            "x-xsrf-token": requests.utils.unquote(self.session.cookies["XSRF-TOKEN"]),
        }
        self.__number = ""

    def generate_number(self, countries=["SE","GB","FR","FI","NL","DK"]):
        json = {
            "number": countries
        }
        self.__number = self.session.post("https://smsnator.online/generate-number", json=json, headers=self.headers).json()["number"]

    def get_number(self):
        return self.__number

    def get_inbox(self, wait=False):
        json = {
            "number": self.__number
        }
        inbox = lambda : self.session.post("https://smsnator.online/message-list", json=json, headers=self.headers).json()
        if wait:
            while len(inbox()) == 1:
                time.sleep(1)
        return inbox()[1:]

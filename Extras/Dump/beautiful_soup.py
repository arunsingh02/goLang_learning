import os
from bs4 import BeautifulSoup
import requests

URL = "https://realpython.github.io/fake-jobs/"

def get_url_data():
    response = requests.get(URL)
    return response.content

if __name__ == '__main__':
    print(get_url_data())

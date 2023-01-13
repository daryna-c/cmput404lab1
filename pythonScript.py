import requests
import sys

print("Requests version:", requests.__version__)
r = requests.get("https://www.google.com/")

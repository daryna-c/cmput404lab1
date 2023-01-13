import requests

print("Requests version:", requests.__version__)
r = requests.get("https://www.google.com/")

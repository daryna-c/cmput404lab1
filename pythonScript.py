import requests

r = requests.get("https://raw.githubusercontent.com/daryna-c/cmput404lab1/main/pythonScript.py")
print("pythonScript source code:\n")
print(r.text)

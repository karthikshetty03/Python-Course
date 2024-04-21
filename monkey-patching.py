import requests


# Monkey patching
def get(url: str):
    return f'{url}:<TEST RESPONSE>'


requests.get = get
data = requests.get('https://www.apple.com')
print(data)

import requests

# API_KEY = input("API key: ")
#
# params = {
#     "X-API-KEY"
# }


url = input("URL: ")
data = requests.get(url).json()
if data:
    while True:
        for key in data:
            print(key)

        goto = input("GOTO: ")
        data = data[goto]
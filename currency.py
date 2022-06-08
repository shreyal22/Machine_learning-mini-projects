import requests
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8b3cff2e1d2dfd79de05"

res = requests.get(url)

data = res.json()
print(data['USD_INR'])

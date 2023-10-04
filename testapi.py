import requests

url = 'https://5665xca6le.execute-api.us-east-1.amazonaws.com/prod/graph'
myobj = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}

x = requests.post(url, json = myobj)

print(x.text)
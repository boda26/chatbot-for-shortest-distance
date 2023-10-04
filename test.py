import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
	"graphApi": 'https://5665xca6le.execute-api.us-east-1.amazonaws.com/prod/graph', #<post api for storing the graph>,
	"botName": 'graphbot', # <name of your Amazon Lex Bot>, 
	"botAlias": 'graphbot', # <alias name given when publishing the bot>,
	"identityPoolId": 'us-east-1:174a5b41-42de-4c1b-871d-1892d08189a3', #<cognito identity pool id for lex>,
	"accountId": '347526106917', #<your aws account id used for accessing lex>,
	"submitterEmail": 'boda2@illinois.edu', # <insert your coursera account email>,
	"secret": 'SPG6RzI3zecyT32x', # <insert your secret token from coursera>,
	"region": 'us-east-1'#<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
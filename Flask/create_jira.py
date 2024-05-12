from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

#create a flask app instance
app = Flask(__name__)

#Decorator=perform action before execution of function
@app.route("/createJIRA",methods=['POST'])
def createJIRA():
    

    url = "https://karthikrkh22.atlassian.net/rest/api/2/issue"

    API_TOKEN="ATATT3xFfGF0-WsX472dOZSDdgW-AUHlVYxglq_wn6UfScFmhnnUy4VLu9qdLFKMjrd_0mbIe-OaYpVED0jzydSz4NYmzCMoR3Z0Y1cqLvrgQINhsccevZZDIBr5_x8Yyy6VGyQMyBTOyovDihEPw3VCauSaMIAQGCuFtlLgHlyu8MlN1SKS1sY=057A3961"
    auth = HTTPBasicAuth("karthikrkh22@gmail.com",API_TOKEN )

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        
        
        
        "description": "Order entry fails when selecting supplier.",
        
        "issuetype": {
        "id": "10019"
        },
        
        
        "project": {
        "key": "DM"
        },
        
        "summary": "Main order flow broken",
        
        
    },
    "update": {
        
    }
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")) 

app.run('0.0.0.0',port=5000)


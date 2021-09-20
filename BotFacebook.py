import json
import requests
from flask import flask, request

VERIFY_TOKEN = "giphy"
app = flask(__name__)
@app.route('/', methods =['GET'])
def verify():
    if(request.args.get('hub.verify_token','')==VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge','')
    else:
        print('wrong verification token')
        return("Error, Verification Failed")
        
        if(__name__=='__main_'):
         app.run(debug=True)


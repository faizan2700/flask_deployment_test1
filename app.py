from flask import Flask 
import azure.cosmos.cosmos_client as cosmos_client 
from dotenv import load_dotenv 
load_dotenv() 
import os 

app = Flask(__name__) 

def run_sample():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent_overwrite=True)
 
@app.route('/') 
def hello_world(): 
    run_sample() 
    return '<h1>Hello World</h1>' 

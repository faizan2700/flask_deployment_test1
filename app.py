from flask import Flask 
import azure.cosmos.cosmos_client as cosmos_client 
from dotenv import load_dotenv 
load_dotenv() 
import os 

app = Flask(__name__) 

HOST = os.getenv('HOST') 
DATABASE_ID = os.getenv('DATABASE_ID') 
CONTAINER_ID = os.getenv('CONTAINER_ID') 
MASTER_KEY = os.getenv('MASTER_KEY')

def run_sample():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent_overwrite=True)
 
@app.route('/') 
def hello_world(): 
    run_sample() 
    return '<h1>Hello World</h1>' 

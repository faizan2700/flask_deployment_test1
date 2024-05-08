from flask import Flask 
import azure.cosmos.cosmos_client as cosmos_client 
from dotenv import load_dotenv 
load_dotenv() 
import os 

app = Flask(__name__) 

# HOST = 'https://third-party-data-store1.documents.azure.com:443/'
# DATABASE_ID = 'database1' 
# CONTAINER_ID = 'example1' 
# MASTER_KEY = 'm4MQPRRqNNt32VLnbRedud4zMjeWwjCuQozLLV9rr7GyLsfQDP0D5CVN6oRdlAychwAM1d3UoP8iACDbc6WUrg=='

def run_sample():
    # client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent_overwrite=True)
    pass 

@app.route('/') 
def hello_world(): 
    run_sample() 
    return '<h1>Hello World</h1>' 

from flask import Flask 
import azure.cosmos.cosmos_client as cosmos_client 

app = Flask(__name__) 

HOST = 'https://third-party-data-store1.documents.azure.com:443/'
string = 'm4MQPRRqNNt32VLnbRedud4zMjeWwjCuQozLLV9rr7GyLsfQDP0D5CVN6oRdlAychwAM1d3UoP8iACDbc6WUrg=='
DATABASE_ID = 'database1'
CONTAINER_ID = 'example1'

def run_sample():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': string}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
    # try:
    #     # setup database for this sample
    #     try:
    #         db = client.create_database(id=DATABASE_ID)
    #         print('Database with id \'{0}\' created'.format(DATABASE_ID))

    #     except exceptions.CosmosResourceExistsError:
    #         db = client.get_database_client(DATABASE_ID)
    #         print('Database with id \'{0}\' was found'.format(DATABASE_ID))

    #     # setup container for this sample
    #     try:
    #         container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))
    #         print('Container with id \'{0}\' created'.format(CONTAINER_ID))

    #     except exceptions.CosmosResourceExistsError:
    #         container = db.get_container_client(CONTAINER_ID)
    #         print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

    #     scale_container(container)
    #     create_items(container)
    #     read_item(container, 'SalesOrder1', 'Account1')
    #     read_items(container)
    #     query_items(container, 'Account1')
    #     replace_item(container, 'SalesOrder1', 'Account1')
    #     upsert_item(container, 'SalesOrder1', 'Account1')
    #     delete_item(container, 'SalesOrder1', 'Account1')

    #     # cleanup database after sample
    #     try:
    #         client.delete_database(db)

    #     except exceptions.CosmosResourceNotFoundError:
    #         pass

    # except exceptions.CosmosHttpResponseError as e:
    #     print('\nrun_sample has caught an error. {0}'.format(e.message))

    # finally:
    #         print("\nrun_sample done")
 
@app.route('/') 
def hello_world(): 
    run_sample() 
    return '<h1>Hello World</h1>' 

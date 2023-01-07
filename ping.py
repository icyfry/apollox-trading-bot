from apollox.rest_api import Client 
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(key=os.environ.get('api_key'), secret=os.environ.get('api_secret'))

# Ping + Timestamp
client.ping()
print(client.time())
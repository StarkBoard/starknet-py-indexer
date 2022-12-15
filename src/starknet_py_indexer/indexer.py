import os
from dotenv import load_dotenv

from core.blocks import transactions_in_block
from core.events import events_in_block
from provider import Provider
load_dotenv()

def start():
    starknet_provider = Provider(os.environ.get('STARKNET_NODE_URL'))
    txs = transactions_in_block("latest", starknet_provider)
    events = events_in_block("latest", starknet_provider)

if __name__== "__main__":
    start()

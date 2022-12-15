import os
from dotenv import load_dotenv

from starknet_py_indexer.core.transactions import transactions_in_block
from starknet_py_indexer.core.events import events_in_block
from starknet_py_indexer.provider import Provider
load_dotenv()

def start():
    starknet_provider = Provider(os.environ.get('STARKNET_NODE_URL'))
    txs = transactions_in_block("latest", starknet_provider)
    events = events_in_block("latest", starknet_provider)

if __name__== "__main__":
    start()

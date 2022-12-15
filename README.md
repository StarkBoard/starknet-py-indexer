# starknet-py-indexer 🗂️

Python Indexer for indexing StarkNet On Chain data

## Getting Started

Create a folder for your project and cd into it:

```
mkdir myproject
cd myproject
```

Create a virtualenv and activate it:

```
python3 -m venv env
source env/bin/activate
```

Install starknet-py-indexer:

```
pip install starknet-py-indexer
```

## Usage

Create a `.env` file in your repository

1. Instantiate a provider

```
starknet_provider = Provider(os.environ.get('STARKNET_NODE_URL'))
```

2. Retrieve block of a given block

```
from core.transactions import transactions_in_block

txs = transactions_in_block("latest", starknet_provider)
txs = transactions_in_block({"block_number": 10}, starknet_provider)
txs = transactions_in_block({"block_hash": "XXXhash"}, starknet_provider)
```

2. Retrieve Events of a given block

```
from core.events import events_in_block

events = events_in_block("latest", starknet_provider)
events = events_in_block({"block_number": 10}, starknet_provider)
events = events_in_block({"block_hash": "XXXhash"}, starknet_provider)
```

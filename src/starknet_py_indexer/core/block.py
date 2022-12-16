import json

def get_block_number(provider):
    """Retrieve the current block number

    Parameters
    ----------
    provider: starknet_py_indexer.Provider
        jsonRPC Provider Instance
    """
    r = provider.post(method="starknet_blockNumber", params=[])
    block_number = json.loads(r.text)["result"]  
    return block_number

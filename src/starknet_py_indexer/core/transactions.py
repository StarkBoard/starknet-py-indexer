import json


def transactions_in_block(block_id, provider):
    """Retrieve the list of transactions from a given block

    Parameters
    ----------
    block_id: BlockId
        block identifier, "latest" or object {"block_number": 1}
    provider: starknet_py_indexer.Provider
        jsonRPC Provider Instance
    """
    r = provider.post(method="starknet_getBlockWithTxs", params=[block_id])
    print(r.text)
    data = json.loads(r.text)
    if 'error'in data:
        return data['error']
    return data["result"]

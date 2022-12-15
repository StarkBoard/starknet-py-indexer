import json


def transactions_in_block(block_id="latest", provider=None):
    """Retrieve the list of transactions from a given block
    """
    r = provider.post(method="starknet_getBlockWithTxs", params=[block_id])
    print(r.text)
    data = json.loads(r.text)
    if 'error'in data:
        return data['error']
    return data["result"]

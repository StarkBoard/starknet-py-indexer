import json

def events_in_block(block_id, provider):
    """Retrieve the list of events in a given block
    """
    params = {
        "filter": {
            "fromBlock": block_id, 
            "toBlock": block_id,
            "chunk_size": 1000
        }
    }
    r = provider.post(method="starknet_getEvents", params=params)
    data = json.loads(r.text)
    if 'error'in data:
        return data['error']
    data = data["result"]
    events = data["events"]
    while data["continuation_token"]:
        params["filter"]["continuation_token"] = data["continuation_token"]
        r = provider.post(method="starknet_getEvents", params=params)
        data = json.loads(r.text)
        if 'error'in data:
            return data['error']
        data = data["result"]
        events += data["events"]
    return events

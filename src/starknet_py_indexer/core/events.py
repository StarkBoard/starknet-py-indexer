import json
from datetime import datetime

def events_in_block(block_id, provider):
    """Retrieve the list of events in a given block

    Parameters
    ----------
    block_id: BlockId
        block identifier, "latest" or object {"block_number": 1}
    provider: starknet_py_indexer.Provider
        jsonRPC Provider Instance
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

def filter_events(events, keys):
    """Filtering events of a given key

    Parameters
    ----------
    events: list
        list of events to filter on
    keys: list
        list of string filter
    """
    filtered_events = list(filter(lambda event: event['keys'][0] in keys, events))
    return filtered_events

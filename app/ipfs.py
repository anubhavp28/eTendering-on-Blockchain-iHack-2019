import ipfsapi

api = ipfsapi.connect('127.0.0.1', 5001)


def upload(filepath):
    res = api.add(filepath)
    return res['Hash']


def download(hash, filepath):
    with open(filepath, "wb") as f:
        f.write(api.cat(hash))
    return

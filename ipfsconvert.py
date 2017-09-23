from flask import Flask
from flask import request
import pdb
import ipfsapi
import requests
app = Flask(__name__)

ipfs = ipfsapi.connect('127.0.0.1', 5001)

@app.route("/contenthash/<multihash>")
def get_content_hash(multihash):
    res = ipfs.add(requests.get("https://gateway.dweb.me/content/contenthash/%s" % multihash))

    requests.get('https://gateway.dweb.me/storeipldhash/contenthash/%s' % res['Hash'])
    return 'ok'

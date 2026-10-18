"""Notify a search engine of published changes. Run only AFTER GitHub Pages deploys.

The IndexNow verification key is intentionally public, served on the website.
It is unrelated to passwords or account API credentials.
"""
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import json
import argparse
import xml.etree.ElementTree as ET

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--engine',choices=['yandex','bing'],default='yandex')
args=parser.parse_args()
endpoint={'yandex':'https://yandex.com/indexnow','bing':'https://www.bing.com/indexnow'}[args.engine]
ROOT=Path(__file__).resolve().parents[1]
config=json.loads((ROOT/'site-config.json').read_text())
key=config['indexnow_key']
pages=[x.text for x in ET.parse(ROOT/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
host=urlsplit(pages[0]).netloc
location='https://'+host+'/'+key+'.txt'
with urlopen(location,timeout=30) as response:
    if response.read().decode('utf-8').strip()!=key:
        raise RuntimeError('The published verification key does not match. Wait for deployment.')
payload={'host':host,'key':key,'keyLocation':location,'urlList':pages}
request=Request(endpoint,data=json.dumps(payload).encode('utf-8'),headers={'Content-Type':'application/json; charset=utf-8'},method='POST')
with urlopen(request,timeout=30) as response:
    status=response.status
    response.read()
if status not in (200,202):
    raise RuntimeError('Unexpected HTTP status: '+str(status))
print(json.dumps({'engine':args.engine,'status':status,'submitted_urls':len(pages),'meaning':'Received' if status==200 else 'Accepted; key verification pending','note':'Submission does not guarantee indexing or ranking.'}))

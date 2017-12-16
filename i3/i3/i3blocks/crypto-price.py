#!/usr/bin/env python3

import sys
import json
import urllib.request

if len(sys.argv) < 2:
    sys.exit()

currency = sys.argv[1]
URL = 'https://api.coinbase.com/v2/prices/{0}-USD/sell'.format(currency)

with urllib.request.urlopen(URL) as req:
    content = json.loads(req.read().decode('utf-8'))
    if not content or 'data' not in content:
        sys.exit()

    if 'amount' not in content['data']:
        sys.exit()

    print('{0} ${1}'.format(currency, int(float(content['data']['amount']))))

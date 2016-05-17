
This project is forked from [Walt Chen](https://github.com/godsarmy/chinese-stock-api/zipball/master).
Mr chen seems do not continue this project.
-----
Library to get Chinese stock price

Supported Engines:
 - Hexun API
 - Sina Finance API
 - Yahoo Finance API

Requirements:
 - Python 2.7.11

Usage:
    
```
from cstock.request import Requests
from cstock.hexun_engine import HexunEngine

engine = HexunEngine()
requester = Requester(engine)

stock = requester.request('000626')
print stock.as_dict()
```


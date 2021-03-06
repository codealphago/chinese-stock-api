import json

from cstock.request import Requester
from cstock.sina_engine import SinaEngine

engine = SinaEngine()
requester = Requester(engine)
# stock = requester.request("00006.HK")
stock = requester.request("002200.SZ")
data = stock[0].as_dict()
print(data)
print(json.dumps(data, ensure_ascii=False))
print(stock[0])
print(data['sell1p'])
print(data['sell1v'])
print(data['buy1p'])
print(data['buy1v'])

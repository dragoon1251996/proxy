
import time
import re
import asyncio
from proxybroker import Broker
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        key=str(proxy.host)+":"+str(proxy.port)
        protocol=re.findall("\[(.*?)\]",str(proxy))[0]
        if "HTTP:" in protocol:
            protocol=re.findall(":(.*?):",":"+protocol)
        else:
            protocol=[x.strip() for x in protocol.split(",")]
        value={"host":str(proxy.host), "port":str(proxy.port),"protocol":protocol,"country":"US"}
        r.set(str(key), value)
        print({key:value})





while True:
    # try:
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(types=["HTTP","HTTPS",'SOCKS4', 'SOCKS5'], countries= "US",limit=500),
        show(proxies))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    # except:
    #     loop.close()
    #     loop = asyncio.new_event_loop()
    #     broker=""
    #     print("x")
    #
    #     pass
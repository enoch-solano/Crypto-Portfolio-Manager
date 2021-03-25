import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from decimal import Decimal

import cbpro
public_client = cbpro.PublicClient()

from dotenv import load_dotenv
load_dotenv()

import os
key =        os.environ.get("key")
b64secret =  os.environ.get("secret")
passphrase = os.environ.get("passphrase")
'''
wsclient =  cbpro.WebsocketClient(url="wss://ws-feed.pro.coinbase.com",
                                 products=["BTC-USD", "ETH-USD"],
                                 channels=["ticker"])
'''



import csv

ONE_MINUTE = 60
ONE_HOUR = 60 * ONE_MINUTE

GRANULARITY = { "ONE_MINUTE" : ONE_MINUTE,
                "FIVE_MINUTES" : 5 * ONE_MINUTE,
                "FIFTEEN_MINUTES" : 15 * ONE_MINUTE,
                "ONE_HOUR" : ONE_HOUR,
                "SIX_HOURS" : 6 * ONE_HOUR,
                "ONE_DAY" : 24 * ONE_HOUR }

MSG_KEYS = { "type" :       0,  # 
             "sequence" :   1,  # 
             "product_id" : 2,  # 
             "price" :      3,  # 
             "open_24h" :   4,  # 
             "volume_24h" : 5, 
             "low_24h" :    6,
             "high_24h" :   7,
             "volume_30d" : 8,
             "best_bid" :   9,
             "best_ask" :   10,
             "side" :       11,
             "time" :       12,
             "trade_id" :   13,
             "last_size" :  14} # 
fig = plt.figure()
ax = plt.axes()
price_data = np.empty([0,1])
time_data = np.empty([0,1])
#{'type': 'ticker', 'sequence': 15200900829, 'product_id': 'ETH-USD', 'price': '1589.31', 'open_24h': '1654.09', 'volume_24h': '277506.33275701', 'low_24h': '1545.77', 'high_24h': '1740.91', 'volume_30d': '7248589.50437355', 'best_bid': '1589.30', 'best_ask': '1589.31', 'side': 'buy', 'time': '2021-03-25T00:56:47.741899Z', 'trade_id': 94365990, 'last_size': '0.00564336'}
class my_wsclient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD"] #, "ETH-USD", "LTC-USD"]
        self.channels = ["ticker"]
        print(" Subscribed to WebSocket feed")

    def on_message(self, msg):
        #might plot here instead
        #print( msg.get("product_id"), " " , msg.get("price"), " " ,msg.get("time"))
        #np.append(price_data, msg.get("price"))
        #np.append(time_data, msg.get("time"))
        
        plt.scatter(msg.get("time"), msg.get("price"))
        #line.set_data(msg.get("time"), msg.get("price"))

        plt.pause(0.0001)
        #print(msg)

    def on_close(self):
        print("closing...")

def main():
    '''
    # 1) using the CB-API
    hist_rates = auth_client.get_product_historic_rates('BTC-USD',
                                                          start=None, end=None,
                                                          granularity = GRANULARITY["ONE_DAY"])

    # 2) parsing the CB-API
    time_data = [np.datetime64(hist_rate[HIST_RATES_KEYS["time"]], 's') for hist_rate in hist_rates]
    price_data = [hist_rate[HIST_RATES_KEYS["close"]] for hist_rate in hist_rates]

    # 3) make plot
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(time_data, np.array(price_data));

    # 4) display plot
    plt.show()

    # 5) store historical data
    with open('database/btc_historical_data.csv', mode='w+') as csv_file:
        fieldnames = ['datetime', 'closing_price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for datetime, price in zip(time_data, price_data):
            writer.writerow({ 'datetime' : datetime, 'closing_price' : price })

    '''
    wsclient = my_wsclient()
    wsclient.start()
    #ani = FuncAnimation(fig, wsclient.start, 1)
    print(wsclient.url, wsclient.products)
    plt.show()

if __name__ == '__main__':
    main()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

import cbpro
public_client = cbpro.PublicClient()

ONE_MINUTE = 60
ONE_HOUR = 60 * ONE_MINUTE

GRANULARITY = { "ONE_MINUTE" : ONE_MINUTE,
                "FIVE_MINUTES" : 5 * ONE_MINUTE,
                "FIFTEEN_MINUTES" : 15 * ONE_MINUTE,
                "ONE_HOUR" : ONE_HOUR,
                "SIX_HOURS" : 6 * ONE_HOUR,
                "ONE_DAY" : 24 * ONE_HOUR }

HIST_RATES_KEYS = { "time" :    0,  # unix timestamp of bucket start time
                    "low" :     1,  # lowest price during the bucket interval
                    "high" :    2,  # highest price during the bucket interval
                    "open" :    3,  # opening price (first trade) in the bucket interval
                    "close" :   4,  # closing price (last trade) in the bucket interval
                    "volume" :  5 } # volume of trading activity during the bucket interval

def main():
    # 1) using the CB-API
    hist_rates = public_client.get_product_historic_rates('BTC-USD',
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


if __name__ == '__main__':
    main()

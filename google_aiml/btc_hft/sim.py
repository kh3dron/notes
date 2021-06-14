#import robin_stocks
from datetime import datetime, time
from time import sleep
import random
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

#I WILL COME BACK TO THIS MESS AFTER I'M DONE WITH THE COURSE
#I KNOW IT SUCKS


def pprint(a):
    return (datetime.utcfromtimestamp(a[0]).strftime('%Y-%m-%d %H:%M') + ":" + str(a[1]))

def dateConv(a):
    return (datetime.utcfromtimestamp(a).strftime('%Y-%m-%d %H:%M'))

def linearAverage(prices):
    return sum(prices)/len(prices)

def r(f): #keeps the printing pretty
    return round(f, 5)

train_df = pd.read_csv("../../bitstampUSD_1-min_data_2012-01-01_to_2020-12-31.csv")

unix_start = 1496275200
#simStart = int((unix_start - 1483228800) / 60)

#Hyperparameters: Buy a dip, sell at gain
dip = .8 
gain = 4

#this shit gutted
def test(dip, gain):

    # For Crypto
    openingPrice = trial[0][1]
    print("Starting Time / Price:", pprint(trial[0]))
    dbg = 5  # Rounding len for printing long numbers less anoyingly

    cur_price = openingPrice
    price_history = []
    price_history.append(openingPrice)

    # Market bools
    bull_1m = True
    bull_1h = True
    bull_1d = True
    bull_7d = True
    bull_1m = True


    seedCap = date1[1] 
    bot_USD = seedCap
    bot_BTC = 0
    trade_limit = 1440*1 #Max trade frequency - every 3 days
    pot_cool = trade_limit
    count_trades = 0

    last_exit = 10**10
    entry = 0

    bot_balance = []
    bot_b_days = []
    trade_enters = []
    trade_exits = []

    i = 0
    while i < simLife:

        if (i % (60*24) == 0):
            #print(" - Day ", i//(60*24), "-") 
            bot_b_days.append(bot_balance)

        if (i == 0):
            cur_price = openingPrice 
        else:
            cur_price = price_history[i-1]

        # Some minutes are missing price data: this if stataement catches that and smoothes over those missinig moments.
        if trial[i][1] != trial[i][1]:
            i += 1
            price_history.append(price_history[-1])
            bot_balance.append(bot_USD+(bot_BTC*price_history[i]))
            continue  # Skips
        else:
            price_history.append(trial[i][1])
            bot_balance.append(bot_USD+(bot_BTC*price_history[i]))

        if i>0:         bull_1m = (cur_price > price_history[i])
        if i>60:        bull_1h = (cur_price > price_history[i-60])
        if i>1440:      bull_1d = (cur_price > price_history[i-1440])
        if i>1440*7:    bull_7d = (cur_price > price_history[i-(1440*7)])
        if i>1440*30:   bull_1m = (cur_price > price_history[i-(1440*30)])

        #TRADE LOOP

        #Buy condition
        if bot_USD > 0 and cur_price < last_exit*dip:
            alloc = bot_USD
            debit = alloc/cur_price
            bot_BTC += debit
            bot_USD -= alloc
            
            pot_cool = trade_limit
            count_trades += 1
            trade_enters.append(i)
            entry = cur_price
            #print("Bought", r(alloc), "USD worth for Debit of", r(debit), "BTC")
        
        #Sell condition
        elif cur_price > entry*gain and bot_USD == 0:
            salloc = bot_BTC
            credit = salloc * cur_price
            bot_USD += credit
            bot_BTC = 0

            pot_cool = trade_limit
            last_exit = cur_price
            count_trades += 1
            trade_exits.append(i)
            #print("Sold", r(salloc), "BTC worth For Credit of", r(debit), "USD")


        pot_cool -= 1
        i = i + 1

    #Debug output to shot performance
    def performanceCheck():
        print("Sim Start:           ", dateConv(date1[0]))
        print("Sim End:             ", dateConv(date2[0]))
        print("Held BTC Return:     ", round(
            ((date2[1] - date1[1])/date1[1])*100, 5), "%")
        print()
        print("Start balance:       ", seedCap)
        print("Cold Balance:        ", round(bot_USD, 2))
        print("Hot Balance:         ", round(bot_BTC*date2[1], 2))
        print("Return (USD Gross):  ", bot_USD+(bot_BTC*date2[1])-seedCap)
        g = bot_USD+(bot_BTC*date2[1])
        print("Return (Rate):       ", round(((g-seedCap)/seedCap), 5)*100, "%")
        print("Count Trades:        ", count_trades)

        plt.style.use('dark_background')
        plt.title("Botting v. Holding: " + dateConv(date1[0]) + " to " + dateConv(date2[0]))
        plt.plot(price_history, label="BTC Price")
        plt.plot(bot_balance, markevery=trade_enters, label="Tradebot Returns")
        plt.legend()
        plt.show()

    ret = ((bot_USD+(bot_BTC*date2[1])-seedCap)/seedCap)
    hodl = ((date2[1] - date1[1])/date1[1])
    
    return ret/hodl


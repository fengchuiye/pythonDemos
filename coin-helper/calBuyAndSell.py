#import math
import sys


def calBuy(origin_price, loop=6, ratio_step=0.02, cash=300):
    print("advices for BUY origin_price is ",origin_price)
    ratio = 0 
    for i in range(loop):
        percent = (1 - ratio)
        tmp = origin_price * percent
        ratio = ratio + ratio_step 
        print(percent * 100,"% is ",format(tmp,'0.8f'),
        "need buy num: ",format(cash/tmp,'0.8f'))

def calSell(origin_price, loop=10, ratio_step=0.01):
    print("advices for SELL origin_price is ",origin_price)
    ratio = ratio_step
    for i in range(loop):
        percent = (1 + ratio)
        tmp = origin_price * percent
        ratio = ratio + ratio_step 
        print(format(percent * 100,'0.2f'),"% is ",format(tmp,'0.8f'))

#print(sys.argv[0]," ",sys.argv[1])
price=float(sys.argv[1])
calBuy(price)
calSell(price)

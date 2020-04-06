import dicimal

coinname = ['USDJPY','EURJPY','AUDJPY','GBPJPY','NZDJPY','ZARJPY']
dic =[]


for coinnames in sample_raw_data: 
    
    if (coinnames['currencyPairCode'] in coinname):
        dic.append(coinnames)

 #if (coinnames['currencyPairCode'] <= coinname[5]だとなぜかうまくいかない   

print(dic)

"""
coinnames['currencyPairCode'] == coinname[0]
    or coinnames['currencyPairCode'] == coinname[1]
    or coinnames['currencyPairCode'] == coinname[2]
    or coinnames['currencyPairCode'] == coinname[3]
    or coinnames['currencyPairCode'] == coinname[4]
    or coinnames['currencyPairCode'] == coinname[5]

#これをこうやって書き換える。

# もし  currencyPairCode が           coinname の中にあれば
  if   coinnames['currencyPairCode'] in coinname:

"""

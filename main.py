from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
cryptocurrencies = cg.get_coins_markets("usd")
n=int(input())
def market_cap_sort():
    list = []
    i = 0
    while i < n:
        list.append(cryptocurrencies[i]['name'])
        i = i + 1
    return list

print(market_cap_sort())
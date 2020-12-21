import json
import requests
#import time

class index():

    def address(self):
        token = self
        if token == "WETH":
            contract = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
        if token == "WBTC":
            contract = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"
        if token == "USDC":
            contract = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
        if token == "DAI":
            contract = "0x6b175474e89094c44da98b954eedeac495271d0f"
        if token == "UNI":
            contract = "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
        if token == "LINK":
            contract = "0x514910771af9ca656af840dff83e8264ecf986ca"
        if token == "ESD":
            contract = "0x36f3fd68e7325a35eb768f1aedaae9ea0689d723"
        if token == "AMPL":
            contract = "0xd46ba6d942050d489dbd938a2c909a5d5039a161"
        if token == "AAVE":
            contract = "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9"
        if token == "YFI":
            contract = "0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e"
        if token == "USDT":
            contract = "0xdac17f958d2ee523a2206206994597c13d831ec7"
        if token == "UST":
            contract = "0xa47c8bf37f92abed4a126bda807a7b7498661acd"
        if token == "CORE":
            contract = "0x62359ed7505efc61ff1d56fef82158ccaffa23d7"
        if token == "BAC":
            contract = "0x3449fc1cd036255ba1eb19d65ff4ba2b8903a69a"
        if token == "DPI":
            contract = "0x1494ca1f11d487c2bbe4543e90080aeba4ba3c2b"
        if token == "HEZ":
            contract = "0xeef9f339514298c6a857efcfc1a762af84438dee"
        if token == "LRC":
            contract = "0xbbbbca6a901c926f240b89eacb641d8aec7aeafd"
        if token == "YFI":
            contract = "0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e"
        if token == "FARM":
            contract = "0xa0246c9032bc3a600820415ae600c6388619a14d"
        if token == "wANATHA":
            contract = "0x3383c5a8969dc413bfddc9656eb80a1408e4ba20"
        if token == "BOND":
            contract = "0x0391d2021f89dc339f60fff84546ea23e337750f"
        if token == "PICKLE":
            contract = "0x429881672b9ae42b8eba0e26cd9c73711b891ca5"
        if token == "MKR":
            contract = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
        if token == "TUSD":
            contract = "0x0000000000085d4780b73119b644ae5ecd22b376"
        if token == "renBTC":
            contract = "0xeb4c2781e4eba804ce9a9803c67d0893436bb27d"
        if token == "TRU":
            contract = "0x4c19596f5aaff459fa38b0f7ed92f11ae6543784"
        return contract

    def convert(self):
        url = self
        req = requests.get(url)
        content = json.loads(req.content)
        raw = json.dumps(content, indent=4, sort_keys=True)
        return raw


class coingecko():

    def pricebtc(self,key = ""):
        raw = index.convert("https://api.coingecko.com/api/v3/exchange_rates")
        new = raw.find(self)
        if key != "":
            currentpricedata = raw[new:new + 135]
            new2 = currentpricedata.find(key)
            new = new + new2
            print(raw[new - 1:new + 20])
        if key == "":
            print(raw[new-1:new+50])
        return self, key

    def tokenprice(self, pair="usd", market_cap="true", twentyfourhr_vol="true", twentyfourhr_change="true",
                   last_updated_at="true"):
        api = "https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses="
        contract = index.address(self)
        # Daten brauchbar machen
        url = str(api) + str(contract) + "&vs_currencies=" + \
                  pair + "&include_market_cap=" + market_cap + "&include_24hr_vol=" + \
                  twentyfourhr_vol + "&include_24hr_change=" + twentyfourhr_change + \
                  "&include_last_updated_at=" + last_updated_at
        raw = index.convert(url)
        return raw


class Anyblock:
    def contractinfo(self):
        address = index.address(self)
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer 1f2bd092-9df5-404b-bf9b-88b96a108d7c',
        }
        response = requests.get('https://api.anyblock.tools/ethereum/ethereum/mainnet/token/'+address, headers=headers)
        content = json.loads(response.content)
        raw = json.dumps(content, indent=4, sort_keys=True)
        return raw

#print(coingecko.pricebtc("usd","LINK"))
#print(coingecko.tokenprice("LINK","eur"))
#print(Anyblock.contractinfo("LINK"))
#print(coingecko.whichadress("LINK"))
#print(coingecko.pricebtc("LINK"))
from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

print("实时Gas监控 (Gwei)")
while True:
    gas = w3.eth.gas_price
    gwei = w3.from_wei(gas, "gwei")
    print(f"{time.ctime()} | Gas价格: {gwei:.2f} Gwei")
    time.sleep(8)

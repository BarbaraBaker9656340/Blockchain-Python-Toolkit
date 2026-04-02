from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
last_block = 0

print("开始监听新区块...")
while True:
    current = w3.eth.block_number
    if current != last_block:
        print(f"✅ 新区块高度: {current} | 时间: {time.ctime()}")
        last_block = current
    time.sleep(5)

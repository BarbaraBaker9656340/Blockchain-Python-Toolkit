from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a9324d24" # BAYC

abi = '[{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"}]'
contract = w3.eth.contract(address=contract_address, abi=abi)

def listen_events():
    print("监听NFT转账事件...")
    while True:
        events = contract.events.Transfer.get_logs(fromBlock="latest")
        for e in events:
            print(f"NFT转账: {e.args}")
        time.sleep(10)

if __name__ == "__main__":
    listen_events()

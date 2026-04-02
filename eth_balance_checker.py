from web3 import Web3

# 连接以太坊RPC
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

# 批量查询余额
def check_balances(addresses):
    for addr in addresses:
        if not w3.is_address(addr):
            continue
        balance = w3.eth.get_balance(addr)
        eth_balance = w3.from_wei(balance, "ether")
        print(f"地址: {addr}\n余额: {eth_balance:.6f} ETH\n")

if __name__ == "__main__":
    address_list = [
        "0x00000000219ab540356cBB839Cbe05303d7705Fa",
        "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    ]
    check_balances(address_list)

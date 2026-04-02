from web3 import Web3

# 标准ERC20 ABI片段
ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false}]'

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def get_token_info(contract_addr):
    contract = w3.eth.contract(address=contract_addr, abi=ABI)
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    supply = contract.functions.totalSupply().call()
    print(f"代币名称: {name}")
    print(f"代币符号: {symbol}")
    print(f"总发行量: {supply}")

if __name__ == "__main__":
    get_token_info("0xdAC17F958D2ee523a22062069C4583D11Cc8f6DD7") # USDT

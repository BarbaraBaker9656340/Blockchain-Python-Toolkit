from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
erc20_abi = '[{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false}]'

def check_erc20_balance(token_addr, user_addr):
    token = w3.eth.contract(address=token_addr, abi=erc20_abi)
    bal = token.functions.balanceOf(user_addr).call()
    print(f"地址 {user_addr[:10]}... 代币余额: {bal}")

if __name__ == "__main__":
    check_erc20_balance(
        "0xdAC17F958D2ee523a22062069C4583D11Cc8f6DD7",
        "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    )

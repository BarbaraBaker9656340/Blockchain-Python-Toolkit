from eth_account import Account
from mnemonic import Mnemonic

# 批量生成ETH钱包
def generate_wallets(count=5):
    mnemo = Mnemonic("english")
    for i in range(count):
        words = mnemo.generate(strength=128)
        Account.enable_unaudited_hdwallet_features()
        acct = Account.from_mnemonic(words)
        print(f"===== 钱包 {i+1} =====")
        print(f"助记词: {words}")
        print(f"地址: {acct.address}")
        print(f"私钥: {acct.key.hex()}\n")

if __name__ == "__main__":
    generate_wallets(3)

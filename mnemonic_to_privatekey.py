from eth_account import Account

Account.enable_unaudited_hdwallet_features()

def mnemonic_to_key(words):
    try:
        acct = Account.from_mnemonic(words)
        print(f"地址: {acct.address}")
        print(f"私钥: {acct.key.hex()}")
        return acct
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    mnemonic = "your twelve word mnemonic phrase here test test test test"
    mnemonic_to_key(mnemonic)

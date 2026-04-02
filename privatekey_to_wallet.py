from eth_account import Account

def privatekey_to_wallet(private_key):
    try:
        acct = Account.from_key(private_key)
        print(f"地址: {acct.address}")
        print(f"私钥: {acct.key.hex()}")
        return acct
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    privatekey_to_wallet("0x1234567890123456789012345678901234567890123456789012345678901234")

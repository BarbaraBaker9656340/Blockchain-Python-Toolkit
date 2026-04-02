from eth_account import Account
from eth_account.messages import encode_defunct

def verify_signature(message, signature, address):
    msg = encode_defunct(text=message)
    recovered = Account.recover_message(msg, signature=signature)
    print(f"签名地址: {recovered}")
    print(f"验证结果: {recovered.lower() == address.lower()}")

if __name__ == "__main__":
    verify_signature(
        "I love blockchain",
        "0x...",
        "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    )

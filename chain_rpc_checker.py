import requests

def check_rpc(rpc_url):
    try:
        data = {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
        res = requests.post(rpc_url, json=data, timeout=5)
        block = int(res.json()["result"], 16)
        print(f"✅ {rpc_url} 正常 | 最新区块: {block}")
        return True
    except:
        print(f"❌ {rpc_url} 不可用")
        return False

if __name__ == "__main__":
    check_rpc("https://rpc.ankr.com/eth")
    check_rpc("https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161")

import requests

def get_nft_metadata(uri):
    try:
        res = requests.get(uri, timeout=10)
        data = res.json()
        print("NFT名称:", data.get("name"))
        print("NFT描述:", data.get("description"))
        print("图片:", data.get("image"))
        return data
    except:
        print("获取失败")

if __name__ == "__main__":
    get_nft_metadata("https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/1")

def decode_hex_data(hex_data):
    try:
        data = hex_data.replace("0x", "")
        method = data[:8]
        params = data[8:]
        print(f"方法ID: 0x{method}")
        print(f"参数: {params}")
        return method, params
    except:
        print("解码失败")
        return None, None

if __name__ == "__main__":
    tx_data = "0xa9059cbb000000000000000000000000d8da6bf26964af9d7eed9e03e53415d37aa96045000000000000000000000000000000000000000000000000000000003b9aca00"
    decode_hex_data(tx_data)

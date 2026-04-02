def calculate_apr(daily_rate, days=365):
    apr = daily_rate * days
    apy = (1 + daily_rate) ** days - 1
    print(f"日利率: {daily_rate*100:.2f}%")
    print(f"APR: {apr*100:.2f}%")
    print(f"APY: {apy*100:.2f}%")

if __name__ == "__main__":
    calculate_apr(0.001)  # 0.1% 日利率

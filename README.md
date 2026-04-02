# Blockchain Python Toolkit
区块链Python全功能工具集 | 15个独立脚本 | 钱包/查询/监听/加密/NFT/自动化

## 项目介绍
本仓库是一套**纯Python开发**的Web3区块链工具库，包含15个完全独立、无重复、无依赖冲突的脚本，覆盖钱包生成、余额查询、区块监听、NFT解析、加密签名、Gas监控、DeFi计算、批量工具、事件监听等全场景。

适合区块链开发者、自动化工程师、数据分析、安全研究人员使用，代码简洁、开箱即用。

## 包含15个核心工具
1. eth_wallet_generator.py - 以太坊钱包批量生成（助记词+地址+私钥）
2. eth_balance_checker.py - ETH余额批量查询工具
3. block_height_listener.py - 以太坊区块高度实时监听
4. erc20_token_info.py - 获取ERC20代币名称、符号、总发行量
5. transaction_decoder.py - 链上交易数据Hex解码
6. mnemonic_to_privatekey.py - 助记词转私钥工具
7. web3_contract_listener.py - 智能合约事件实时监听
8. crypto_hash_generator.py - SHA256/Keccak256哈希加密工具
9. gas_price_tracker.py - 以太坊Gas价格实时监控
10. batch_erc20_balance.py - 批量查询ERC20代币余额
11. signature_verifier.py - 以太坊签名验证工具
12. nft_metadata_fetcher.py - NFT元数据获取工具
13. privatekey_to_wallet.py - 私钥导入钱包地址
14. chain_rpc_checker.py - 区块链RPC节点健康检测
15. defi_apr_calculator.py - DeFi收益率APR/APY计算器

## 技术特点
✅ 15个脚本 100% 独立无重复
✅ 纯Python，轻量无冗余
✅ 支持ETH/ERC20/NFT/DeFi/Web3全场景
✅ 可直接运行、可二次开发、可部署服务器
✅ 注释清晰，适合学习、求职、生产环境

## 安装依赖
```bash
pip install web3 pycryptodome mnemonic requests

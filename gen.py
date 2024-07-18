import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv("config.txt")

amount = int(os.getenv('GEN_AMOUNT', 100))

w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

for i in range(amount):
    acc, mnemonic = w3.eth.account.create_with_mnemonic()
    key = w3.to_hex(acc.key)
    print(f'account={acc.address} | key={key} | seed={mnemonic}')

    with open("addrs.txt", "a") as myfile:
        myfile.write(acc.address+'\n')

    with open("keys.txt", "a") as myfile:
        myfile.write(key+'\n')

    with open("seeds.txt", "a") as myfile:
        myfile.write(mnemonic+'\n')
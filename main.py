import time

from web3 import Web3

with open('private_key.txt', 'r') as pvk:
    private_key = pvk.read().strip()  # Your private key
with open('wallet_address.txt', 'r') as wa:
    wallet_address = Web3.to_checksum_address(wa.read().strip())  # Your public key (wallet address)

web3 = Web3(Web3.HTTPProvider('https://rpc.mainnet.dbkchain.io/'))
nonce = web3.eth.get_transaction_count(wallet_address)


def mint():
    tx = {
        'chainId': web3.eth.chain_id,
        'data': '0x1249c58b',
        'from': wallet_address,
        'to': Web3.to_checksum_address('0x633b7472E1641D59334886a7692107D6332B1ff0'),
        'nonce': nonce,
        'gasPrice': web3.eth.gas_price,
    }

    gas = web3.eth.estimate_gas(tx)
    tx.update({'gas': gas})

    signed_txn = web3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f'https://scan.dbkchain.io/tx/{tx_hash.hex()}')


while True:
    try:
        mint()
        nonce += 1
    except Exception as err:
        print(err)
        time.sleep(10)

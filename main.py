import random

from web3 import Web3

private_key = ''  # Your private key
wallet_address = Web3.to_checksum_address('')  # Your public key (wallet address)

web3 = Web3(Web3.HTTPProvider('https://rpc.mainnet.dbkchain.io/'))
nonce = web3.eth.get_transaction_count(wallet_address)


def mint():
    tx = {
        'chainId': web3.eth.chain_id,
        'data': '0x1249c58b',
        'from': wallet_address,
        'to': Web3.to_checksum_address('0x633b7472E1641D59334886a7692107D6332B1ff0'),
        'nonce': nonce,
        'maxFeePerGas': int(0.000001 * 10**9),
        'maxPriorityFeePerGas': int(0.000001 * 10**9)
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

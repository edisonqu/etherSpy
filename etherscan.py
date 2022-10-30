import requests
import datetime
from dotenv import load_dotenv
from sendSMS import send_message
import os

load_dotenv()

def etherscan_txs(address):
    etherscan_api = os.getenv("etherscan_api")
    # address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    start_block = 0
    end_block = 99999999
    sort = 'desc'
    offset = 1

    # Starting the unique search for Blocks
    blockNumber = ''
    old_blockNumber = ''
    counter = 0
    while counter < 100:
        response = requests.get(f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={start_block}&endblock={end_block}&page=1&offset={offset}&sort={sort}&"
                                f"apikey={etherscan_api}")
        # result = response["result"]
        res = response.json()

        result = res['result']

        if len(result) == 0:
            continue

        # print(block_number)
        first_result = result[0]
        blockNumber = first_result['blockNumber']
        hash = first_result['hash']
        time = datetime.datetime.fromtimestamp(int(first_result['timeStamp']))
        block_hash = first_result['blockHash']
        txs_from = first_result['from']
        txs_to = first_result['to']
        txs_value = int(first_result['value'])

        if blockNumber != old_blockNumber:
            if txs_value == 0:
                message = f"ALERT: User: {txs_from} interacted with User: {txs_to} on {time}. See more information on https://etherscan.io/tx/{hash}."
            else:
                message = f"ALERT: User: {txs_from} transacted {txs_value} to User: {txs_to} on {time}. See more information on https://etherscan.io/tx/{hash}."

            send_message(message)

        old_blockNumber =  blockNumber
        counter+=counter+1

    return "finished"


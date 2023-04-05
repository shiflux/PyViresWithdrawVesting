import pywaves as pw
import requests
import simplejson
from consts import *

class VestingWithdrawal:
    def __init__(self,  seed):
        self.tries = WITHDRAW_MAX_TRIES_DAY
        try:
            pw.setNode(node = WAVES_NODE, chain = WAVES_CHAN)
        except Exception as e:
            print("Error connecting to node")
            print(e)
        try:
            self.address = pw.Address(seed = seed)
        except Exception as e:
            print("Private key error")
            print(e)
            exit()

    def withdraw(self):
        print('withdrawing...')
        try:
            tx = self.address.invokeScript(VIRES_CONTRACT,
                                           VIRES_VESTING_WITHDRAWAL_COMMAND,
                                           VIRES_VESTING_WITHDRAWAL_ARGS,
                                           [],
                                           txFee=WAVES_TRANSACTION_FEE
                                           )
            
            print(tx)
            if 'error' in tx:
                print('tx error')
                return False
            else:
                self.tries -= 1
                print('tries remaining: {}'.format(self.tries))
                return True
        except Exception as e:
            print(e)
            return False

    def check_vesting(self):
        try:
            height = self.get_block_height()

            if height % WAVES_DAY_BLOCKS in [0, 1, 2]:
                if self.tries == 0:
                    return False

                result = simplejson.loads(requests.get(VIRES_VESTING_API.format(self.address.address)).text)
                if not result:
                    return False
                
                # result is in microusd
                available_today = int(result['availableToday'])/1000000
                available_today_global = int(result['globallyAvailableToday'])/1000000
                
                if available_today>0:
                    if available_today_global>0:
                        return self.withdraw()
                    else:
                        print("No money available for withdrawal :(")
                        return False
                else:
                    print("Already withdrawed today :)")
                    return False
            else:
                self.tries = WITHDRAW_MAX_TRIES_DAY
                print('{} blocks left to withdraw'.format(WAVES_DAY_BLOCKS - (height%WAVES_DAY_BLOCKS)))
                return False
        except Exception as e: 
            print(e)
            return False

    def import_vtoken(self, amount, token):
        try:
            height = self.get_block_height()

            if height % WAVES_DAY_BLOCKS in [WAVES_DAY_BLOCKS-1, 0]:
                print('importing...')
                tx = self.address.invokeScript(VIRES_IMPORT_CONTRACT,
                                            VIRES_IMPORT_COMMAND,
                                            [],
                                            [
                                                {"amount": amount,"assetId": token}
                                                ],
                                            txFee=WAVES_TRANSACTION_FEE_IMPORT
                                            )
                print(tx)
                return True
            print('{} blocks left to import'.format(WAVES_DAY_BLOCKS - (height%WAVES_DAY_BLOCKS)))
            return False
        except Exception as e:
            print(e)
            return False

    def import_USDTLP(self, amount):
        return self.import_vtoken(amount, VIRES_USDTLP_ADDRESS)

    def import_USDCLP(self, amount):
        return self.import_vtoken(amount, VIRES_USDCLP_ADDRESS)

    def get_block_height(self):
        result = simplejson.loads(requests.get(''.join([WAVES_NODE, WAVES_HEIGHT_API])).text)
        if not result:
                return None
        return int(result['height'])
    
    def unstake_token(self, token, amount):
        try:
            tx = self.address.invokeScript(VIRES_UNSTAKE_CONTRACT,
                                        VIRES_UNSTAKE_COMMAND,
                                        [
                                            {
                                                "type":"string",
                                                "value": VIRES_TOKEN_ADDRESSES[token],
                                            },
                                            {
                                                "type": "integer",
                                                "value": amount
                                            }
                                        ],
                                        [],
                                        txFee=WAVES_TRANSACTION_FEE_IMPORT
                                        )
            print(tx)
            return True
        except Exception as e:
            print(e)
            return False

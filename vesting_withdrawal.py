import pywaves as pw
import requests
import simplejson
from consts import *

class VestingWithdrawal:
    def __init__(self,  seed):
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
            return True
        except Exception as e:
            print(e)
            return False

    def check_vesting(self):
        try:
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

        except Exception as e: 
            print(e)
            return False

    def import_vtoken(self, amount, token):
        print('importing...')
        try:
            tx = self.address.invokeScript(VIRES_IMPORT_CONTRACT,
                                           VIRES_IMPORT_COMMAND,
                                           [],
                                           [
                                            {"amount": amount,"assetId": token}
                                            ],
                                           txFee=WAVES_TRANSACTION_FEE
                                           )
            print(tx)
            return True
        except Exception as e:
            print(e)
            return False

    def import_USDTLP(self, amount):
        return self.import_vtoken(amount, VIRES_USDTLP_ADDRESS)

    def import_USDCLP(self, amount):
        return self.import_vtoken(amount, VIRES_USDTLP_ADDRESS)
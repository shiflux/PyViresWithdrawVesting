from pywaves import DEFAULT_INVOKE_SCRIPT_FEE
WAVES_NODE = 'https://nodes.wavesexplorer.com'
WAVES_CHAN = 'mainnet'
WAVES_TRANSACTION_FEE = DEFAULT_INVOKE_SCRIPT_FEE
VIRES_CONTRACT = '3PCbvPVQfSvVu88ip8Fm5YjwJhjEYk1Txhk'
VIRES_VESTING_WITHDRAWAL_COMMAND = 'withdrawVestedAllUSDN'
VIRES_VESTING_WITHDRAWAL_ARGS = [
    {"type": "boolean", "value": False},
    {"type": "boolean",  "value": True},
    ]
VIRES_VESTING_API='https://api.vires.finance/user/{}/vesting/markets'

try:
    from local_consts import *
except ImportError:
    pass
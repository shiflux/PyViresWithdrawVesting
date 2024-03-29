from pywaves import DEFAULT_INVOKE_SCRIPT_FEE
WAVES_NODE = 'https://nodes.wavesexplorer.com'
WAVES_CHAN = 'mainnet'
WAVES_HEIGHT_API = '/blocks/height'
WAVES_TRANSACTION_FEE = DEFAULT_INVOKE_SCRIPT_FEE
WAVES_TRANSACTION_FEE_IMPORT = DEFAULT_INVOKE_SCRIPT_FEE
WAVES_DAY_BLOCKS = 1440

VIRES_CONTRACT = '3PCbvPVQfSvVu88ip8Fm5YjwJhjEYk1Txhk'
VIRES_IMPORT_CONTRACT = '3PAZv9tgK1PX7dKR7b4kchq5qdpUS3G5sYT'
VIRES_VESTING_WITHDRAWAL_COMMAND = 'withdrawVestedAllUSDN'
VIRES_IMPORT_COMMAND = 'replenishWithAtoken'
VIRES_VESTING_WITHDRAWAL_ARGS = [
    {"type": "boolean", "value": False},
    {"type": "boolean",  "value": True},
    ]
VIRES_VESTING_API='https://api.vires.finance/user/{}/vesting/markets'
VIRES_USDTLP_ADDRESS = '2tVLdi5fQXk2JcuDAojhctnDp5B5PZhNMyj5GUpeC3tZ'
VIRES_USDCLP_ADDRESS = 'FSRHtSyXRXQjzQLRtmaqFpBDDCNjY8PU8KNtwoGXVBmr'
VIRES_LEGACY_DEPOIST_API = 'https://vires-api.vercel.app/api/evaluate/3PKZk5TdPCLP2GZviipLFfK46ExTnwkRCBd/adviseUser/{}'

LOOP_TIME = 60

WITHDRAW_MAX_TRIES_DAY = 1

VIRES_UNSTAKE_CONTRACT = '3PAZv9tgK1PX7dKR7b4kchq5qdpUS3G5sYT'
VIRES_UNSTAKE_COMMAND = 'withdraw2'
VIRES_TOKEN_ADDRESSES = {
    'eth': '3PPdeWwrzaxqgr6BuReoF3sWfxW8SYv743D',
    'btc': '3PA7QMFyHMtHeP66SUQnwCgwKQHKpCyXWwd',
    'xtn': '3PCwFXSq8vj8iKitA5zrrLRbuqehfmimpce',
}

try:
    from local_consts import *
except ImportError:
    pass

from vesting_withdrawal import VestingWithdrawal
import time
import argparse
import consts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', type=str, help='Seed phrase', required=True)
    parser.add_argument('-w', '--withdraw', help='Set option to withdraw vesting', required=False, action='store_true')
    parser.add_argument('-t', '--token', type=str, help='Token to import', required=False)
    parser.add_argument('-a', '--amount', type=int, help='Amount of token to import', required=False)
    args = parser.parse_args()
    vw = VestingWithdrawal(seed=args.seed)
    
    while True:
        res = False
        if args.withdraw:
            res = vw.check_vesting()
        if args.token and args.amount:
            if args.token.lower() == 'usdt':
                vw.import_USDTLP(args.amount)
            elif args.token.lower() == 'usdc':
                vw.import_USDCLP(args.amount)
        time.sleep(res if res else consts.LOOP_TIME)
        
if __name__ == '__main__':
    main()

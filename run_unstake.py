
from vesting_withdrawal import VestingWithdrawal
import time
import argparse
import consts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', type=str, help='Seed phrase', required=True)
    parser.add_argument('-t', '--token', type=str, help='Token to unstake (ETH, BTC)', required=True)
    parser.add_argument('-a', '--amount', type=int, help='Amount of token to import', required=True)
    args = parser.parse_args()
    vw = VestingWithdrawal(seed=args.seed)
    
    while True:
        vw.unstake_token(args.token.lower(), args.amount)
        time.sleep(consts.LOOP_TIME)
        
if __name__ == '__main__':
    main()

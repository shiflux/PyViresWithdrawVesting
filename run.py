
from vesting_withdrawal import VestingWithdrawal
import time
import argparse
import consts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', type=str, help='Seed phrase', required=True)
    args = parser.parse_args()
    vw = VestingWithdrawal(seed=args.seed)
    
    while True:
        vw.check_vesting()
        time.sleep(consts.LOOP_TIME)
        
if __name__ == '__main__':
    main()

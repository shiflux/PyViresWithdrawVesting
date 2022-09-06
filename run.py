
from vesting_withdrawal import VestingWithdrawal
import time
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', type=str, help='Seed phrase', required=True)
    args = parser.parse_args()
    vw = VestingWithdrawal(seed=args.seed)
    
    while True:
        vw.check_vesting()
        time.sleep(60)
        
if __name__ == '__main__':
    main()
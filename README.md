# Table of Contents
1. [Installation](README.md#installation)
2. [Instructions](README.md#instructions)
3. [Licensing](README.md#license)

# Installation
- 1.1 Install pipenv env
```
pipenv install
```

# Instructions:
## USDN vesting withdrawal
Run the following command, where 'my seed phrase' is your address seed
```
python run.py -w -s 'my seed phrase'
```

## Import USDT/USDC LP tokens
Run the following command, where:
- 'my token' is the desired token, 'usdt' or 'usdc'
- 'amount' is the amount to import. The base value is multiplied by 1000000
- 'my seed phrase' is your address seed

```
python run.py -t 'my token' -a 'amount' -s 'my seed phrase'
```

eg. Will try to import 100 USDTLP
```
python run.py -t usdt -a 100000000 -s 'my seed phrase'
```

This function does not check if it can import or not, so run it for brief periods or it will burn all the waves with fees.

# License
You can use this in any way you want.
from bit import Key

key = Key()
# como criar uma carteira?
wallet = key.address
print(f'my wallet: {wallet}')

saldo = key.get_balance()
print(f'meu saldo: {saldo}')
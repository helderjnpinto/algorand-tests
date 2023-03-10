from utils.faucet import dispense



dispense_tx = dispense("MH5IDGBKUC2GB6OJ6WKFW6KQA7E55MHBKEYJMZ64OYTI5VJXNMCEWEGHGM", 1_000_000)
print('\033[91m'+'dispense_tx: ' + '\033[92m', dispense_tx)

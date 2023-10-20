from eth_account import Account
import threading

Account.enable_unaudited_hdwallet_features()

def is_valid_end(address, valid_words):
    lowercase_address = address.lower()
    lowercase_valid_words = [word.lower() for word in valid_words]
    
    for word in lowercase_valid_words:
        if lowercase_address.endswith(word):
            return True
    return False

def is_valid_start(address, valid_words):
    lowercase_address = address.lower()
    lowercase_valid_words = [word.lower() for word in valid_words]
    
    for word in lowercase_valid_words:
        if lowercase_address[2:].startswith(word):
            return True
    return False
    
def is_valid_address(address, valid_words):
    return is_valid_start(address, valid_words) and is_valid_end(address, valid_words)


def generate_wallets(valid_words):
    while True:
        acct, mnemonic = Account.create_with_mnemonic()
        address = acct.address
        private_key = acct._private_key.hex()
        if is_valid_address(address, valid_words):
            print("Address:", address)
            print("Mnemonic:", mnemonic)
            print("Private Key:", private_key)
            print()

valid_words = [
    "B00B", "F00D", "DADA", "FACED", "DEAD", "BEBE", "FACADE", "ADDED",
    "FADE", "CAFE", "C0FFEE", "BAD", "BAD00", "BED0", "BEEF", "FACE2FACE",
    "B0A", "00F", "B00F", "B00BA", "B00DA", "B00B5", "B0CAFE", "CAFE0",
    "00FF", "BABE","C0DE","DEC0DE","DEFACED","DEFACE"
]

# Nombre de threads à exécuter (a augmenter en fonction de ton PC)
num_threads = 8

threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=generate_wallets, args=(valid_words,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

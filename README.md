# generate-custom-BIP39-ETH-addresses

Ce script Python génère des wallets Ethereum (Private Key, Public Key, Mnemonic) et filtre les adresses en fonction de critères spécifiques. Il utilise la bibliothèque `eth_account` pour créer des portefeuilles Ethereum. Ces wallets personnalisés s'appellent également vanity address

## Installation

Pour exécuter ce script, assurez-vous d'avoir Python installé sur votre système. Vous pouvez installer la bibliothèque `eth_account` en utilisant pip :

```bash
pip install eth-account
```
## Utilisation

Clonez ce repo votre ordinateur :

```bash
git clone https://github.com/gasape51/generate-custom-BIP39-ETH-addresses.git
```
Exécutez le script Python :


```bash
python generate_wallets.py
```

Le script générera des portefeuilles Ethereum et affichera les détails des wallets (Private Key, Public Key, Mnemonic) qui correspondent aux mots clés personnalisés dans la liste valid_words. Vous pouvez personnaliser la liste valid_words en ajoutant ou supprimant des mots-clés selon vos préférences.

Note : Le nombre de threads à exécuter est défini dans la variable num_threads. Vous pouvez ajuster ce nombre en fonction des capacités de votre ordinateur.

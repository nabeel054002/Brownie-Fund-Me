##fns that are always used, like get_account(), are placed here, and the whole thing can always be copy-pasted everytime


from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

decimals = 8
startingprice = 20000000000000
FORKED_BLOCKCHAINS = ['mainnet-fork','mainnet-fork-dev']
LOCAL_BLOCKCHAIN_NETWORKS = ['development','ganache-local']
##we are trying to make the contents of the ganache blockchain visible

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_NETWORKS or network.show_active() in FORKED_BLOCKCHAINS:
        return accounts[0]
        ##but the mainnet fork does not have the accounts variable...
        ##mainnet forking is much better on alchemy than infura
    else:
        return accounts.add(config["wallets"]["from_key"])
def deploy_mocks():
    if len(MockV3Aggregator) <=0:
        mock_aggregator = MockV3Aggregator.deploy(decimals,Web3.toWei(startingprice,"Ether"),{'from':get_account()})
##closing the ganache folder does mean that you will be closing the local blockchain
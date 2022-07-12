##first writing to deploy to rinkeby chain and then the local ganache chain

from brownie import FundMe,MockV3Aggregator,accounts, config, network
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks
)

LOCAL_BLOCKCHAIN_NETWORKS = ['development','ganache-local']
##we are trying to make the contents of the ganache blockchain visible...

def deploy_contract():
    account = get_account()
    print(f'the length is {len(FundMe)}')
    #FundMe.deploy({'from':account})
    #print(len(FundMe))
    if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS:
        priceFeedaddress = config['networks'][network.show_active()]['ethusdt_price']
    else:
        print(f"The active network is {network.show_active()}")
        deploy_mocks()
        ##now here we are on a local blockchain, i.e. a development network
        print('mocks deployed')
        priceFeedaddress = MockV3Aggregator[-1].address
    fund_contract = FundMe.deploy(priceFeedaddress,{'from':account}, publish_source = config['networks'][network.show_active()]['abc'])
    print(f'the length is {len(FundMe)}')
    return fund_contract

##we want to verify the thing on etherscan and publish it for ease of intereaction ig, follow steps in the vid
##the whole contract is in hexcode on etherscan

def main():
    deploy_contract()
##what does it mean to verify code ...


##now to deploy it onto ganache
##we need to create a local price feed, there are 2 ways to get around this:
# - forking or - mocking

##mocking is deploying a fake version of the same thing and interacting as though if it were real
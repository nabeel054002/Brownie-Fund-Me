
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_NETWORKS
#LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_contract
from brownie import network, accounts, exceptions
import pytest

def test_can_fund():
    account = get_account()
    fund_me = deploy_contract()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

def test_can_withdraw():
    account = get_account()
    fund_me = deploy_contract()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    print('first subtest passed')
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
    print('second subtest passed')

    ##i would be going with one assert in each function
    ##the default network is the development one

def get_entr():
    account = get_account()
    fund_me = deploy_contract()
    print('why is this thing not even reaching here')
    #print(f'the contract is {fund_me}')

def test_only_ownercan_withdraw():
    ##since running tests on the testnet or mainnet can take up a lot of time, hence why we use pytest`s skip functionality`
    owner = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS:
        pytest.skip("i am only testing for the local blockchain environments")
    fund_me = deploy_contract()
    badactor = accounts.add()
    print("badactor ---------------", badactor)
    fund_me.fund({'from':owner, 'value': fund_me.getEntranceFee()})
    print(f" the amount owner address has sent is - {fund_me.addressToAmountFunded(owner)}")
    #with pytest.raises(exceptions.VirtualMachineError):
        ##if the following content raises that error, then the following testing function passes...
    fund_me.withdraw({"from": str(badactor)})
        ##iska alag natak hai


###imp stuff
##riority 1 to have all tests passed on a local spun up ganache blockchain
##and then testnets - which is called as integration testing...

##brownie mainnet forking is optional... other stuff as mentioned in the video
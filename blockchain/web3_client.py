from web3 import Web3
from agent.config import Config

class Web3Client:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER_URI))
        if self.web3.is_connected():  
            print("Connected to Ethereum network")
        else:
            raise ConnectionError("Failed to connect to Ethereum network")

    def get_coin_balance(self, address):
        """Get the balance of an address in native coin (e.g., ETH or ZIL)."""
        balance = self.web3.eth.get_balance(address)
        return self.web3.from_wei(balance, 'ether')

    def get_contract(self, contract_address, abi):
        """Get a contract instance for the provided address and ABI."""
        return self.web3.eth.contract(address=contract_address, abi=abi)

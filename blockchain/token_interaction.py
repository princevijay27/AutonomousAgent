from blockchain.web3_client import Web3Client
from agent.config import Config

class TokenInteraction:
    def __init__(self, web3_client: Web3Client, token_address: str, abi: dict):
        self.web3_client = web3_client
        self.token_contract = self.web3_client.get_contract(token_address, abi)

    def get_token_balance(self, address: str) -> int:
        """Get the balance of an address for the ERC-20 token."""
        balance = self.token_contract.functions.balanceOf(address).call()
        return balance

    def get_coin_and_token_balance(self, address: str):
        """Get both the native coin and ERC-20 token balance of an address."""
        coin_balance = self.web3_client.get_coin_balance(address)
        token_balance = self.get_token_balance(address)
        print(f"Coin Balance (Ether/ZIL) for {address}: {coin_balance}")
        print(f"Token Balance for {address}: {token_balance}")
        return coin_balance, token_balance

    def transfer_tokens(self, from_address, to_address, amount, private_key):
        """Transfer tokens from one address to another."""
        txn = self.token_contract.functions.transfer(to_address, amount).build_transaction({
            'chainId': Config.CHAIN_ID,  # Adjust if using a testnet
            'gas': Config.GAS_LIMIT,
            'gasPrice': self.web3_client.web3.eth.gas_price,
            'nonce': self.web3_client.web3.eth.get_transaction_count(from_address),
        })

        # Sign the transaction
        signed_txn = self.web3_client.web3.eth.account.sign_transaction(txn, private_key=private_key)

        # Send the signed transaction
        txn_hash = self.web3_client.web3.eth.send_raw_transaction(signed_txn.raw_transaction)  # Use raw_transaction
        print(f"Transaction hash: {txn_hash.hex()}")
        return txn_hash.hex()


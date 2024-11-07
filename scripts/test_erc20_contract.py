import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blockchain.web3_client import Web3Client
from blockchain.token_interaction import TokenInteraction
from agent.config import Config
from tests.fixtures import get_token_abi

def test_balances():
    """Test fetching both coin and token balance of the source address."""
    web3_client = Web3Client()
    TOKEN_ABI = get_token_abi()  
    token_interaction = TokenInteraction(web3_client, Config.TOKEN_CONTRACT_ADDRESS, TOKEN_ABI)
    
    coin_balance, token_balance = token_interaction.get_coin_and_token_balance(Config.SOURCE_ADDRESS)
    print(f"Source Address Coin Balance: {coin_balance}")
    print(f"Source Address Token Balance: {token_balance}")

if __name__ == "__main__":
    test_balances()

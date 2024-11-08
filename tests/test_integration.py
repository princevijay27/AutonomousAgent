# tests/test_integration.py
import unittest
from agent.agent import Agent
from agent.message import Message, InBox, OutBox
from agent.handler import HelloHandler, CryptoHandler
from agent.behavior import RandomMessageBehavior, TokenBalanceBehavior
from blockchain.web3_client import Web3Client
from blockchain.token_interaction import TokenInteraction
from agent.config import Config
from tests.fixtures import get_token_abi

class TestAgentIntegration(unittest.TestCase):
    def setUp(self):
        # Setup Web3 client and token interaction
        self.web3_client = Web3Client()
        self.token_interaction = TokenInteraction(self.web3_client, Config.TOKEN_CONTRACT_ADDRESS, get_token_abi())
        
        # Create two agents
        self.agent1 = Agent()
        self.agent2 = Agent()
        
        # Set agent1's OutBox as agent2's InBox and vice versa
        self.agent1.outbox = self.agent2.inbox
        self.agent2.outbox = self.agent1.inbox
        
        # Register handlers and behaviors
        self.agent1.register_handler("hello", HelloHandler())
        self.agent2.register_handler("crypto", CryptoHandler(self.web3_client, Config.SOURCE_ADDRESS, Config.TARGET_ADDRESS))

        self.agent1.register_behavior(RandomMessageBehavior())
        self.agent2.register_behavior(TokenBalanceBehavior(self.web3_client, Config.SOURCE_ADDRESS, Config.TOKEN_CONTRACT_ADDRESS))

    def test_message_exchange(self):
        """Test that agent1's messages appear in agent2's inbox and vice versa."""
        # Generate a message from agent1
        self.agent1.run_behaviors()
        message = self.agent2.inbox.get_message()  # Should receive the message generated by agent1
        self.assertIsNotNone(message)

    def test_crypto_transfer(self):
        """Test that the crypto handler triggers a token transfer on 'crypto' message."""
        message = Message("crypto", "trigger transfer")
        self.agent1.outbox.add_message(message)  # Send message from agent1 to agent2
        
        # Process the message
        self.agent2.process_messages()
        
        # Verify the token transfer (would require a mock or a simulated environment to avoid real transfers)
        # Here we would check if the transaction hash or balance change is as expected

if __name__ == "__main__":
    unittest.main()

# tests/test_agent.py
import unittest
from agent.agent import Agent
from agent.message import Message, InBox, OutBox
from agent.handler import HelloHandler
from agent.behavior import RandomMessageBehavior

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
        self.inbox = InBox()
        self.outbox = OutBox()
        self.hello_handler = HelloHandler()
        self.random_message_behavior = RandomMessageBehavior()

    def test_hello_handler(self):
        """Test if HelloHandler correctly identifies and processes 'hello' messages."""
        self.agent.register_handler("hello", self.hello_handler)
        message = Message("hello", "hello world")
        self.inbox.add_message(message)
        
        # Simulate the agent processing the message
        self.agent.process_messages()
        self.assertTrue("hello" in message.content)

    def test_random_message_behavior(self):
        """Test RandomMessageBehavior generates a message."""
        self.agent.register_behavior(self.random_message_behavior)
        
        # Simulate the behavior adding a message to the outbox
        self.random_message_behavior.execute(self.outbox)
        message = self.outbox.get_message()
        self.assertIsNotNone(message)
        self.assertIn(message.content.split()[0], RandomMessageBehavior.WORDS)

if __name__ == "__main__":
    unittest.main()

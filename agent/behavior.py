import random
import time
from agent.message import Message
from datetime import datetime

class Behavior:
    def execute(self, outbox):
        """Execute the behavior. To be implemented by subclasses."""
        raise NotImplementedError("Must be implemented by subclasses.")

class RandomMessageBehavior:
    def __init__(self):
        self.interval = 2  # Every 2 seconds

    WORDS = ["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"]

    def execute(self, inbox):
        """Generate a random two-word message and add it to the inbox."""
        while True:
            # Generate a random two-word message
            content = " ".join(random.sample(self.WORDS, 2))

            
            if "hello" in content and "crypto" in content:
                continue
            
            if "crypto" in content:
                message_type = "crypto"
            elif "hello" in content:
                message_type = "hello"
            else:
                message_type = "random"

            # Create and add the message to the inbox
            message = Message(type=message_type, content=content)
            inbox.add_message(message)
            # print(f"Random message generated: {content} (type: {message_type})")
            print(f"[{datetime.now()}] Random message generated: {content} (type: {message_type})")

            break

class TokenBalanceBehavior:
    def __init__(self, token_interaction, address):
        self.token_interaction = token_interaction
        self.address = address
        self.interval = 10  # Execute every 10 seconds

    def execute(self, outbox):
        """Check the ERC-20 token balance and print it."""
        balance = self.token_interaction.get_token_balance(self.address)
        # print(f"Token balance for {self.address}: {balance}")
        print(f"[{datetime.now()}] Token balance for {self.address}: {balance}")
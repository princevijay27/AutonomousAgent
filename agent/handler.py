from agent.message import Message

class MessageHandler:
    def handle(self, message: Message):
        """Handle a specific message. To be implemented by subclasses."""
        raise NotImplementedError("Must be implemented by subclasses.")

class HelloHandler(MessageHandler):
    def handle(self, message: Message):
        """Handle messages containing 'hello'."""
        if "hello" in message.content:
            print("HelloHandler received:", message)

class CryptoHandler:
    def __init__(self, token_interaction, source_address, target_address, private_key):
        self.token_interaction = token_interaction  
        self.source_address = source_address
        self.target_address = target_address
        self.private_key = private_key

    def handle(self, message: Message):
        """Handle 'crypto' messages by initiating a token transfer."""
        print("CryptoHandler received a message:", message)
        print("Message content:", message.content)
    
        if message.type == "crypto":
            print("Processing crypto message for transfer")
            amount = 10 ** 18  # Assuming 1 token with 18 decimals;
            print(f"Initiating token transfer of {amount} from {self.source_address} to {self.target_address}")

            try:
                # Call transfer_tokens on token_interaction instead of web3_client
                transaction_hash = self.token_interaction.transfer_tokens(
                    self.source_address, self.target_address, amount, self.private_key
                )
                print(f"Token transfer initiated. Transaction hash: {transaction_hash}")
            except Exception as e:
                print(f"Failed to initiate token transfer: {e}")

import queue
from typing import Optional

class Message:
    def __init__(self, type: str, content: str):
        self.type = type
        self.content = content

    def __str__(self):
        return f"Message(type={self.type}, content={self.content})"

class InBox:
    def __init__(self):
        self.messages = queue.Queue()

    def add_message(self, message: Message):
        """Add a message to the inbox."""
        self.messages.put(message)

    def get_message(self) -> Optional[Message]:
        """Retrieve a message from the inbox if available."""
        if not self.messages.empty():
            return self.messages.get()
        return None

class OutBox:
    def __init__(self):
        self.messages = queue.Queue()

    def add_message(self, message: Message):
        """Add a message to the outbox."""
        self.messages.put(message)

    def get_message(self) -> Optional[Message]:
        """Retrieve a message from the outbox if available."""
        if not self.messages.empty():
            return self.messages.get()
        return None


# agent/agent.py

import threading
import time
from agent.message import InBox, OutBox, Message
from agent.handler import MessageHandler
from agent.behavior import Behavior

class Agent:
    def __init__(self):
        self.inbox = InBox()
        self.outbox = OutBox()
        self.handlers = {}
        self.behaviors = []
        self._stop_event = threading.Event()

    def register_handler(self, message_type: str, handler: MessageHandler):
        """Register a handler for a specific message type."""
        self.handlers[message_type] = handler

    def register_behavior(self, behavior: Behavior):
        """Register a behavior to execute proactively."""
        self.behaviors.append(behavior)

    def process_messages(self):
        """Continuously process messages from the inbox."""
        while not self._stop_event.is_set():
            message = self.inbox.get_message()
            if message:
                handler = self.handlers.get(message.type)
                if handler:
                    handler.handle(message)
                else:
                    print(f"No handler registered for message type: {message.type}")
            time.sleep(0.1)  # Add a small delay to prevent high CPU usage

    def run_behavior(self, behavior, interval):
        """Run a behavior at its specified interval."""
        while not self._stop_event.is_set():
            behavior.execute(self.inbox)
            time.sleep(interval)

    def start(self):
        """Start the agent's message processing and behavior execution."""
        self._message_thread = threading.Thread(target=self.process_messages)
        self._message_thread.start()
        
        # Start each behavior in its own thread
        for behavior in self.behaviors:
            interval = behavior.interval if hasattr(behavior, 'interval') else 1
            threading.Thread(target=self.run_behavior, args=(behavior, interval)).start()

    def stop(self):
        """Stop the agent's threads gracefully."""
        self._stop_event.set()
        self._message_thread.join()

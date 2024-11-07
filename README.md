## Project Title: Autonomous Agent with Token Interaction

### Overview

This project implements an autonomous agent capable of handling asynchronous messages and performing specific behaviors, such as generating random messages, checking an ERC-20 token balance, and initiating token transfers on receiving specific commands. Built with Python, Web3, and configurable settings, this agent is designed for blockchain interactions on Ethereum or compatible networks.

### Features

- **Random Message Generation**: Generates random two-word messages from a specified set every 2 seconds.
- **Message Handling**:
  - **HelloHandler**: Responds to messages containing the keyword `"hello"` by printing the message.
  - **CryptoHandler**: Triggers a token transfer when a message containing `"crypto"` is received.
- **Token Balance Check**: Checks the ERC-20 token balance of a specified address every 10 seconds and prints it.
- **Configurable Environment**: Key parameters like chain ID and gas limit are configurable via `.env`.

### Prerequisites

- Python 3.7+
- Install required Python packages:

  ```bash
  pip install -r requirements.txt
  ```

- **Environment Variables**: Define necessary variables in a `.env` file in the project root.

### Setup and Configuration

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a `.env` file**:
   Add the following environment variables to your `.env` file:

   ```plaintext
   WEB3_PROVIDER_URI=<your_web3_provider_url>
   PRIVATE_KEY=<your_private_key>
   SOURCE_ADDRESS=<your_source_address>
   TARGET_ADDRESS=<your_target_address>
   TOKEN_CONTRACT_ADDRESS=<your_token_contract_address>
   CHAIN_ID=<your_chain_id>  # Example: 33101 for a testnet
   GAS_LIMIT=<gas_limit>  # Example: 200000
   ```

3. **Update the ABI**:
   Replace the placeholder `TOKEN_ABI` in `run_agent.py` with the actual ABI for your ERC-20 token contract.

### Project Structure

```
├── agent/
│   ├── agent.py                  # Main agent class handling behaviors and handlers
│   ├── behavior.py               # Defines autonomous behaviors
│   ├── handler.py                # Defines message handlers for "hello" and "crypto" keywords
│   └── config.py                 # Loads configuration from .env file
├── blockchain/
│   ├── web3_client.py            # Initializes Web3 client
│   └── token_interaction.py      # Token interaction functions (balance check, transfer)
├── scripts/
│   └── run_agent.py              # Script to run the agent
├── tests/
│   ├── test_agent.py             # Unit tests for agent functionality
│   └── test_integration.py       # Integration tests for end-to-end functionality
├── .env                          # Environment configuration file (not tracked in version control)
└── README.md                     # Project documentation
```

### Running the Agent

1. **Start the Agent**:
   ```bash
   python scripts/run_agent.py
   ```

2. **Expected Console Output**:
   - Every 2 seconds: Random messages generated.
   - Every 10 seconds: ERC-20 token balance printed for `SOURCE_ADDRESS`.
   - When `"hello"` appears in a message, `HelloHandler` prints the message.
   - When `"crypto"` appears in a message, `CryptoHandler` initiates a token transfer and prints the transaction hash.

### Example Output

```plaintext
Connected to Ethereum network
Starting the agent...
Random message generated: hello universe (type: hello)
HelloHandler received: Message(type=hello, content=hello universe)
Token balance for 0x93764eC0D0162Ec579a506b923CFf427bE17dAab: 999999000000000000000000
Random message generated: crypto moon (type: crypto)
CryptoHandler received: Message(type=crypto, content=crypto moon)
Processing crypto message for transfer
Transaction hash: <transaction_hash>
```

### Testing

Run unit and integration tests using the following command:

```bash
python -m unittest discover tests
```

### Customization

- **Adjust Chain ID and Gas Limit**: Modify `CHAIN_ID` and `GAS_LIMIT` in the `.env` file as needed.
- **Add New Behaviors or Handlers**: You can extend `behavior.py` and `handler.py` to add more autonomous behaviors or message handlers.

### Troubleshooting

- **"GasPrice lower than minimum allowable" Error**: Increase the gas price setting in `web3_client.py`.
- **Missing ABI**: Make sure the `TOKEN_ABI` for the ERC-20 token is correctly added.


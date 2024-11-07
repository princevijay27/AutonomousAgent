import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
    SOURCE_ADDRESS = os.getenv("SOURCE_ADDRESS")
    TARGET_ADDRESS = os.getenv("TARGET_ADDRESS")
    TOKEN_CONTRACT_ADDRESS = os.getenv("TOKEN_CONTRACT_ADDRESS")
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "10"))
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")  
    TENDERLY_API_KEY = os.getenv("TENDERLY_API_KEY")
    CHAIN_ID = int(os.getenv("CHAIN_ID", 33101))  # Default to 1 if not provided
    GAS_LIMIT = int(os.getenv("GAS_LIMIT", 200000))  # Default to 200000 if not provided

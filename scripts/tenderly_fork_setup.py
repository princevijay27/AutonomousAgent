import requests
import os

TENDERLY_API_KEY = os.getenv("TENDERLY_API_KEY")
TENDERLY_USER = "your_tenderly_username"
TENDERLY_PROJECT = "your_tenderly_project"

def create_fork():
    """Creates a new Tenderly fork."""
    url = f"https://api.tenderly.co/api/v1/account/{TENDERLY_USER}/project/{TENDERLY_PROJECT}/fork"
    headers = {
        "X-Access-Key": TENDERLY_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "network_id": "1"  
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        fork_data = response.json()
        print(f"Fork created successfully! Fork ID: {fork_data['simulation_fork']['id']}")
        print("Fork RPC URL:", fork_data["simulation_fork"]["rpc_url"])
        return fork_data["simulation_fork"]["rpc_url"]
    else:
        print("Failed to create fork:", response.json())
        return None

if __name__ == "__main__":
    rpc_url = create_fork()
    if rpc_url:
        print("Use this RPC URL in your Web3 client:", rpc_url)

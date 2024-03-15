from web3 import Web3

# Contract address and ABI
contract_address = '0x1048Eca024cB2Ba5eA720Ac057D804E95a809Fc8'
abi = [
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"}
        ],
        "name": "getRequestIdsByUser",
        "outputs": [
            {"name": "", "type": "uint256[]"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

# Goerli testnet RPC URL
goerli_rpc_url = 'https://goerli.gateway.tenderly.co/16jIpLz5YclxQQCGytcLHP'

# Initialize a web3 connection to the Goerli Testnet
w3 = Web3(Web3.HTTPProvider(goerli_rpc_url))

# Check if connected to the Goerli network
is_connected = w3.is_connected()

# Assuming you are connected, here's how to interact with the contract
if is_connected:
    contract = w3.eth.contract(address=contract_address, abi=abi)
    
    # Replace '0xYourAddress' with the address you want to query
    user_address = '0xYourAddress'
    
    # Call the function from the smart contract
    request_ids = contract.functions.getRequestIdsByUser(user_address).call()
    print(request_ids)
else:
    print("Not connected to Goerli Testnet")

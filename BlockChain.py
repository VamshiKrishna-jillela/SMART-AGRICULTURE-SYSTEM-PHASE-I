from web3 import Web3
from decouple import config
endpoint=config('ENDPOINT')



def conn_(w3):
    if w3.isConnected():
        print("-" * 50)
        print("Connection Successful")
        print("-" * 50)
        return 1
    else:
        print("Connection Failed")
        return 0

def get_contract_object(w3):
    contract_address=config('CONTRACT_ADDRESS')
    abi="""[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newCID",
				"type": "string"
			}
		],
		"name": "pushCID",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "Bihar",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "startIndex",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "size",
				"type": "uint256"
			}
		],
		"name": "getLastKcids",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
     ]"""
    contract = w3.eth.contract(address=contract_address, abi=abi)
    return contract

def get_k_cids(w3,start_index, number_of_cids):
    contract=get_contract_object(w3)
    desired_cid_list=contract.functions.getLastKcids(start_index,number_of_cids).call()
    print(desired_cid_list)
    return desired_cid_list

def get_ith_cid(w3,index):
    contract=get_contract_object(w3)
    desired_cid=contract.functions.Bihar(index).call()
    print(desired_cid)
    return desired_cid

def push_cid(w3,CID):
    contract=get_contract_object(w3)
    from_address=config('CALLER')
    private_key=config('PRIVATE_KEY')
    nonce=w3.eth.get_transaction_count(from_address)
    chain_id=w3.eth.chain_id
    cid_transaction=contract.functions.pushCID(CID).build_transaction({"chainId":chain_id, "from":from_address,"nonce":nonce})
    signed_tnx=w3.eth.account.sign_transaction(cid_transaction,private_key=private_key)
    send_tnx=w3.eth.send_raw_transaction(signed_tnx.rawTransaction)
    tnx_receipt = w3.eth.wait_for_transaction_receipt(send_tnx)
    print(tnx_receipt)
    return tnx_receipt



def insert_cid(cid):
    w3=Web3(Web3.HTTPProvider(endpoint))
    is_success=conn_(w3)
    if(is_success==True):	
        tnx_receipt=push_cid(w3,cid)
        return tnx_receipt
    else:
	    return "connection failed......man"


if __name__ == "__main__":
    w3=Web3(Web3.HTTPProvider(endpoint))
    is_success=conn_(w3)
    if(is_success==True):	
       get_k_cids(w3,0,100)

        
	

        


    
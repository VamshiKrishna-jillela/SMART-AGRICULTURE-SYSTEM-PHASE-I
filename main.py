from BlockChain import insert_cid
from IPFS import uploadToIPFS
import sys
sys.path.insert(0, '/home/vamshi2171/Desktop/temp/INTELLIGENT_ENGINE')
from lstm_test import cropRecommend

if __name__ == "__main__":

    filename="dataUnit.json"

    send={
        "N": "102",
        "P": "101",
        "K": "401",
        "temperature":"203.79744",
        "humidity":"198.002744",
        "ph":"7.902985",
        "rainfall":"110.99"
    }
    #Gives the labelled Data
    Predicted_JSON=cropRecommend(send)
    print(Predicted_JSON)

    #writes the labelled data to a file
    jsonFile = open(filename, "w")
    jsonFile.write(Predicted_JSON)
    jsonFile.close()

    #uploads file to IPFS
    CID=uploadToIPFS(filename)

    #pushes CID to smart Contract
    tnx_receipt=insert_cid(CID)

    print(tnx_receipt)


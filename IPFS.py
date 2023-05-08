import requests, json
from decouple import config

endpoint = "https://ipfs.infura.io:5001"
ProjectId=config('PROJECTID')
ProjectKey=config('PROJECTKEY')


def uploadToIPFS(filename):
    path="./"+filename
    response=requests.post(
        endpoint+'/api/v0/add',
        files={'file':open(path,'rt')},
        auth=(ProjectId,ProjectKey)
    )
    CID=response.json()['Hash']
    print(CID)
    return CID

def retrieveContent(CID):
    response = requests.post(endpoint + '/api/v0/cat', params={'arg':CID}, auth=(ProjectId, ProjectKey)) 
    print(response.text)
    response_json=response.json()
    print(response_json)
    return response_json



retrieveContent('QmfQSUaybpoSV6fRTN2LPdYfgE8w6icLFyFjAmXdzptdkv')

// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.8.17 and less than 0.9.0
pragma solidity ^0.8.19;

contract SmartAgricultutre{
       string[] public Bihar;
       address private owner;


       constructor(){
         owner=msg.sender;
       }


       function pushCID(string calldata newCID) public onlyOwner {
               Bihar.push(newCID);
       }

       

       function getLastKcids(uint startIndex, uint size) view public returns (string[] memory){
          if(Bihar.length-startIndex<size){
              size=Bihar.length-startIndex;
          }
          string[] memory result = new string[](size);
          uint idx=0;
          uint pos=startIndex;
          while(idx<size){
                  result[idx]=Bihar[pos];
                  idx++;
                  pos++;
          } 
          return result;
       }

       function TotalCIDs() view private returns (uint) {
         return Bihar.length;
       }

       modifier onlyOwner(){
               require(msg.sender==owner,"Only the Owner can have the access to Update CID list.");
               _;
       }


}

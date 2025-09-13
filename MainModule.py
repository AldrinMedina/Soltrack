from nicegui import ui
import pymysql
from web3 import Web3
from solcx import compile_source
import json
import os
import datetime
from web3.middleware import ExtraDataToPOAMiddleware
from web3.exceptions import TransactionNotFound


class MainModule:
    def __init__(self):
  
        infura_url = os.getenv ("SEPOLIAAPIKEY")
        private_key  = os.getenv("OWNERPRIVATEKEY")  

        web3 = Web3(Web3.HTTPProvider(infura_url))
        web3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)        
        owner_account = web3.eth.account.from_key(private_key)

        address1 = owner_account.address
        address2 = "0xEb8f64FDf7537086E9E3AA720c7e06217f62156F"  
        address3 = "0xEb8f64FDf7537086E9E3AA720c7e06217f62156F"  

        # Database connection
        mydb = pymysql.connect(
            host= os.getenv("MYSQLHOST"), 
            user= os.getenv("MYSQLUSER"), 
            password = os.getenv("MYSQLPASSWORD"), 
            database = os.getenv("MYSQLDATABASE"))
        mycursor = mydb.cursor()

        solidity_code = '''
pragma solidity  0.5.16;

contract SimpleTransfer {
    event Transfer(address indexed from, address indexed to, uint256 value);

    function Deposit(address payable _to) public payable {
        require(msg.value > 0, "Must send some Ether");
        _to.transfer(msg.value);
        emit Transfer(msg.sender, _to, msg.value);
    }

    function Refund(address payable _to) public payable {
        require(msg.value > 0, "Must send some Ether");
        _to.transfer(msg.value);
        emit Transfer(msg.sender, _to, msg.value);
    }
}
'''

      
        


      

            # Finished Contracts
            with ui.tab_panel(Triarii).classes("fade-in"):
                with ui.column().classes("w-full"):
                    ui.label("Click an action to mark contract status").classes("text-md text-gray-600 mb-2")

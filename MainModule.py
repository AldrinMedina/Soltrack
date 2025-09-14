from nicegui import ui
import psycopg2
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
        address2 = "0x1A947d2CfcF6a4EF915a4049077BfE9acc7Ddb0D"  
        address3 = "0xe6909292b6b108FAa7C8b908d0bD8Efcc57A5078"  

        try:
            mydb = psycopg2.connect(
                host=os.getenv("PGHOST"),
                user=os.getenv("PGUSER"),
                password=os.getenv("PGPASSWORD"),
                database=os.getenv("PGDATABASE"),
                port=os.getenv("PGPORT")
            )
            mycursor = mydb.cursor()
            print("Successfully connected to the PostgreSQL database!")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            mydb = None
            mycursor = None
        
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
        with ui.tabs().classes('w-full shadow-md rounded-xl bg-white text-blue-900') as tabs:
            Primary = ui.tab('Contract Creation')
            Secundus = ui.tab('Ongoing Contracts')
            Triarii = ui.tab('Finished Contracts')

        with ui.tab_panels(tabs, value=Primary).classes('w-full p-6 bg-gray-100 rounded-b-xl shadow-lg'):
            
            # Contract Creation
            with ui.tab_panel(Primary).classes("gap-8 fade-in"):
                with ui.row().classes("w-full justify-between"):
                    with ui.column().classes("bg-white p-4 rounded-xl shadow-md w-1/3"):
                        ui.label("Account Details").classes("text-lg font-semibold mb-2")
                        Eth1 = web3.from_wei(web3.eth.get_balance(address1), 'ether')
                        Eth2 = web3.from_wei(web3.eth.get_balance(address2), 'ether')
                        Eth3 = web3.from_wei(web3.eth.get_balance(address3), 'ether')
                        ui.label(f"Buyer: {Eth1} ETH")
                        ui.label(f"Seller: {Eth2} ETH")
                        ui.label(f"3rd Party: {Eth3} ETH")

                    with ui.column().classes("bg-white p-4 rounded-xl shadow-md w-1/3"):
                        ui.label("Payment Details").classes("text-lg font-semibold mb-2")
                        self.PayAmnt = ui.input(label='Payment Amount', value=20).classes("w-full mb-2")
                        ui.input(label='Service Fee', value=5).classes("w-full mb-1")
                        ui.label("*One-time service charge").classes("text-sm text-gray-500")
                        with ui.row().classes("mt-4 w-full items-center"):
                            ui.label("Select Vaccine").classes("text-md font-medium")
                            self.Vaccine = ui.select(["Pfizer", "Moderna", "AstraZeneca"], value="Pfizer").classes("w-1/4")
                        ui.separator()
                        ui.button("Confirm Contract", on_click=lambda: Deploy(
                            self.FromWhom.value,
                            self.ToWhom.value,
                            self.Vaccine.value,
                            int(self.PayAmnt.value)
                        )).classes("bg-blue-800 text-white hover:bg-blue-900 w-full mt-4")

                    with ui.column().classes("bg-white p-4 rounded-xl shadow-md w-1/3"):
                        ui.label("Contract Info").classes("text-lg font-semibold mb-2")
                        self.FromWhom = ui.input(label='Buyer', placeholder='Your Address', value=address1).classes("w-full mb-2")
                        self.ToWhom = ui.input(label='Seller', placeholder='Seller Address', value=address2).classes("w-full mb-2")
                        ByWhom = ui.input(label='3rd Party', placeholder='3rd Party Address', value=address3).classes("w-full")

            # Ongoing Contracts
            with ui.tab_panel(Secundus).classes("fade-in"):
                with ui.column().classes("w-full"):
                    ui.label("Click an action to mark contract status").classes("text-md text-gray-600 mb-2")
                    if mycursor:
                        mycursor.execute("SELECT Id, Address, CreationDate FROM Contracts WHERE Finished = FALSE")
                        myresult = mycursor.fetchall()
                        with ui.list().props('dense separator'):
                            ui.item_label('Active Contracts').props('header').classes('text-bold text-blue-900')
                            for x in myresult:
                                Id, address, date = x
                                short_address = address[:6] + "..." + address[-4:]
                                with ui.item().classes("hover:bg-gray-200 rounded-lg"):
                                    with ui.item_section():
                                        ui.item_label(f"Contract Address: {short_address}")
                                        ui.item_label(f"Created: {date}")
                                    with ui.item_section().classes("gap-2"):
                                        ui.button("Success", on_click=lambda x=x: ForwardPay(f'{Id}')).classes("bg-green-600 text-white")
                                        ui.button("Refund", on_click=lambda x=x: Refund(f'{Id}')).classes("bg-red-600 text-white")

            # Finished Contracts
            with ui.tab_panel(Triarii).classes("fade-in"):
                with ui.column().classes("w-full"):
                    if mycursor:
                        mycursor.execute("SELECT Address, ActivationDate FROM Contracts WHERE Finished = TRUE")
                        myresult = mycursor.fetchall()
                        with ui.list().props('dense separator'):
                            ui.item_label('Completed Contracts').props('header').classes('text-bold text-blue-900')
                            for x in myresult:
                                address, date = x
                                short_address = address[:6] + "..." + address[-4:]
                                with ui.item().classes("hover:bg-gray-200 rounded-lg"):
                                    with ui.item_section():
                                        ui.item_label(f"Contract Address: {short_address}")
                                        ui.item_label(f"Activated: {date}")

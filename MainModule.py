from nicegui import ui
import pymysql
from web3 import Web3
from solcx import compile_source, compile_standard, install_solc, get_installable_solc_versions, get_solc_version
import json
import os
import datetime


class MainModule:
		def __init__(self):
			ganache_url = "http://127.0.0.1:8545"  
			web3 = Web3(Web3.HTTPProvider(ganache_url))
			accounts = web3.eth.accounts
			mydb = pymysql.connect(
				host=os.getenv("MYSQLHOST"),
				user=os.getenv("MYSQLUSER"),
				password=os.getenv("MYSQLPASSWORD"),
				database=os.getenv("MYSQLDATABASE"),
				port=int(os.getenv("MYSQLPORT", 3306)),
				cursorclass=pymysql.cursors.DictCursor
			)
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
			js_code = '''
async function connectMetaMask() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the connected account
        } catch (error) {
            console.error('User  denied account access:', error);
            return null; // Return null if access is denied
        }
    } else {
        console.log('MetaMask is not installed. Please install it to use this app.');
        return null; // Return null if MetaMask is not installed
    }
}
'''			
			
			def MetaMaskConnect(self, ):
				account = ui.run_javascript(f'''
				{js_code}
				connectMetaMask();
				''')
				if account:
					ui.notify(f'Connected: {account}')
				else:
					ui.notify('Failed to connect to MetaMask.')
			
			def Deploy(From, To, Vacc, Pay  ):
				compiled_sol = compile_source(solidity_code)
				contract_id, contract_interface = compiled_sol.popitem()
				abi = contract_interface['abi']
				bytecode = contract_interface['bin']
				SimpleTransfer = web3.eth.contract(abi=abi, bytecode=bytecode)
				tx_hash = SimpleTransfer.constructor().transact({
				'from': web3.eth.accounts[0] 
				})
				tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
				contract_address = tx_receipt.contractAddress
				abi_json = json.dumps(abi)
				contract = web3.eth.contract(address=contract_address, abi=abi)
				to_address = web3.eth.accounts[2]
				from_address = web3.eth.accounts[0]
				amount = 25
				tx_hash2 = contract.functions.Refund(to_address).transact({
       				'from': from_address,
        			'value': web3.to_wei(amount, 'ether')
   				 })
				web3.eth.wait_for_transaction_receipt(tx_hash2)
				current_datetime = datetime.datetime.now()
				formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')
				sql = "INSERT INTO Contract_Table (Abi, Address, CreationDate, Finished, BuyerAddress, SellerAddress, PaymentAmount, Vaccine) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
				val = (abi_json, contract_address, formatted_datetime, 0, From, To, Pay, Vacc)
				mycursor.execute(sql, val)
				mydb.commit()
				ui.navigate.reload()

			def Refund(IdTarg):
				mycursor.execute(f"SELECT Abi, Address FROM Contract_Table WHERE Id = {IdTarg}")
				ContractInfo = mycursor.fetchone()
				Abi, Address = ContractInfo
				contract = web3.eth.contract(address=Address, abi=Abi)
				to_address = web3.eth.accounts[0]
				from_address = web3.eth.accounts[2]
				amount = 20
				tx_hash = contract.functions.Refund(to_address).transact({
        			'from': from_address,
        			'value': web3.to_wei(amount, 'ether')
    				})
				web3.eth.wait_for_transaction_receipt(tx_hash)
				activation_date = datetime.datetime.now()
				updatequery = "UPDATE Contract_Table SET Finished = %s, ActivationDate = %s WHERE Id = %s"
				mycursor.execute(updatequery, (1,activation_date.strftime('%Y-%m-%d %H:%M'), IdTarg))
				mydb.commit()
				ui.navigate.reload()

			def ForwardPay(IdTarg):
				mycursor.execute(f"SELECT Abi, Address FROM Contract_Table WHERE Id = {IdTarg}")
				ContractInfo = mycursor.fetchone()
				Abi, Address = ContractInfo
				contract = web3.eth.contract(address=Address, abi=Abi)
				to_address = web3.eth.accounts[1]
				from_address = web3.eth.accounts[2]
				amount = 20
				tx_hash = contract.functions.Refund(to_address).transact({
       				 'from': from_address,
        			'value': web3.to_wei(amount, 'ether')
    				})
				web3.eth.wait_for_transaction_receipt(tx_hash)
				activation_date = datetime.datetime.now()
				updatequery = "UPDATE Contract_Table SET Finished = %s, ActivationDate = %s WHERE Id = %s"
				mycursor.execute(updatequery, (1,activation_date.strftime('%Y-%m-%d %H:%M'), IdTarg))
				mydb.commit()
				ui.navigate.reload()


			with ui.tabs().classes('w-full shadow-md rounded-xl bg-white text-blue-900') as tabs:
				Primary = ui.tab('Contract Creation')
				Secundus = ui.tab('Ongoing Contracts')
				Triarii = ui.tab('Finished Contracts')

			with ui.tab_panels(tabs, value=Primary).classes('w-full p-6 bg-gray-100 rounded-b-xl shadow-lg'):
				
				# Contract Creation
				with ui.tab_panel(Primary).classes("gap-8 fade-in"):
					with ui.row().classes("w-full justify-between"):
						with ui.column().classes("bg-white p-4 rounded-xl shadow-md w-1/3"):
							ui.label("Ganache Account Details").classes("text-lg font-semibold mb-2")
							Eth1 = int(web3.from_wei(web3.eth.get_balance(web3.eth.accounts[0]), 'ether'))
							Eth2 = int(web3.from_wei(web3.eth.get_balance(web3.eth.accounts[1]), 'ether'))
							Eth3 = int(web3.from_wei(web3.eth.get_balance(web3.eth.accounts[2]), 'ether'))	
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
							self.FromWhom = ui.input(label='Buyer', placeholder='Your Address', value=web3.eth.accounts[0]).classes("w-full mb-2")
							self.ToWhom = ui.input(label='Seller', placeholder='Seller Address', value=web3.eth.accounts[1]).classes("w-full mb-2")
							ByWhom = ui.input(label='3rd Party', placeholder='3rd Party Address', value=web3.eth.accounts[2]).classes("w-full")

						

					

				# Ongoing Contracts
				with ui.tab_panel(Secundus).classes("fade-in"):
					with ui.column().classes("w-full"):
						ui.label("Click an action to mark contract status").classes("text-md text-gray-600 mb-2")
						mycursor.execute("SELECT Id, Address, CreationDate FROM Contract_Table WHERE Finished = 0")
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
						mycursor.execute("SELECT Address, ActivationDate FROM Contract_Table WHERE Finished = 1")
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
	

from nicegui import ui
import pymysql
from web3 import Web3
from solcx import compile_source, compile_standard, install_solc, get_installable_solc_versions, get_solc_version
import json
import os
import datetime
from web3.middleware import geth_poa_middleware

from web3 import Web3

class MainModule:
    def __init__(self):
        infura_url = "https://sepolia.infura.io/v3/0a916ab0592e408d9c9bee7ff50a2fd6"
        web3 = Web3(Web3.HTTPProvider(infura_url))
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        address1 = "0xEb8f64FDf7537086E9E3AA720c7e06217f62156F"
        address2 = "0xEb8f64FDf7537086E9E3AA720c7e06217f62156F"
        address3 = "0xEb8f64FDf7537086E9E3AA720c7e06217f62156F"
        def Deploy(From, To, Vacc, Pay  ):
            compiled_sol = compile_source(solidity_code)
            contract_id, contract_interface = compiled_sol.popitem()
			abi = contract_interface['abi']
			bytecode = contract_interface['bin']
			SimpleTransfer = web3.eth.contract(abi=abi, bytecode=bytecode)
			tx_hash = SimpleTransfer.constructor().transact({
			    'from': address1
			})
			tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
			contract_address = tx_receipt.contractAddress
			abi_json = json.dumps(abi)
			contract = web3.eth.contract(address=contract_address, abi=abi)
			to_address = address3
			from_address = address1
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
            to_address = address1
            from_address = address3
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
            to_address = address2
            from_address = address3
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
							Eth1 = int(web3.from_wei(address1), 'ether'))
							Eth2 = int(web3.from_wei(address2), 'ether'))
							Eth3 = int(web3.from_wei(address3), 'ether'))	
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

        
    


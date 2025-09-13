from nicegui import ui
import pymysql
from web3 import Web3
from solcx import compile_source, compile_standard, install_solc, get_installable_solc_versions, get_solc_version
import json
import os
import datetime


class MainModule:
	def __init__(self):
		infura_url = "https://sepolia.infura.io/v3/0a916ab0592e408d9c9bee7ff50a2fd6"
		web3 = Web3(Web3.HTTPProvider(infura_url))
		address1 = "0xEb8f64FDf7537086E9E3AA720c7e06217f62156F"
	if web3.is_connected():
		print("Connection to Sepolia RPC successful!")
		balance_wei = web3.eth.get_balance(address)
		balance_eth = web3.from_wei(balance_wei, 'ether')
		print(f"Balance of {address}: {balance_eth} ETH")
	else:
    	print("Connection failed. Check your API key and network status.")

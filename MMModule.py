from nicegui import ui as UI
from HeaderModule import HeaderModule
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
function Bruh() {
alert(1234)
}
'''
async def MetaMaskConnect(self,):
	account = await UI.run_javascript(f'''{js_code} connectMetaMask();''')
	if account:
		UI.notify(f'Connected: {account}')
		
	else:
		UI.notify('Failed to connect to MetaMask.')		
class MMModule:

	def __init__(self):
		with UI.row().style('width: 100%;').classes("justify-center"):
			with UI.card():
				UI.label("MetaMaskConnect")

				with UI.button("Connect", on_click = MetaMaskConnect).style("width:100%;"):
					UI.image("MetaMask.png").classes('rounded-full w-16 h-16 ml-4')
				self.Continue = UI.button("Continue").style("width: 100%;").disable()


UI.run()
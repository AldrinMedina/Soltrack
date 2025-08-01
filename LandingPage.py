from nicegui import ui
from HeaderModule import HeaderModule
from LogInModule import LogInModule
from MMModule import MMModule
from MainModule import MainModule
from FooterModule import FooterModule
from NavBar import NavBar
from solcx import compile_source, compile_standard, install_solc, get_installable_solc_versions

# ui.page_title('Soltrack | Smarter Vaccine Logistics')
# ui.add_head_html('<link rel="preconnect" href="https://fonts.googleapis.com">')
# ui.add_head_html('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap">')
# ui.add_head_html('<style>body { font-family: "Inter", sans-serif; transition: all 0.3s ease-in-out; } .fade-in { opacity: 0; transform: translateY(20px); animation: fadeInUp 0.6s ease forwards; } @keyframes fadeInUp { to { opacity: 1; transform: none; } }</style>')


# --- Navigation Bar ---
# with ui.header().classes('bg-blue-900 text-white p-4 shadow-md justify-between'):
#     with ui.row().classes('items-center '):
#         ui.label('Soltrack').classes('text-xl font-bold')
#     with ui.row().classes('q-gutter-md items-center'):
#         ui.link('Home', '#').classes('text-white hover:underline')
#         ui.link('About', '#').classes('text-white hover:underline')
#         ui.link('Features', '#').classes('text-white hover:underline')
#         ui.link('Demo', '#').classes('text-white hover:underline')
#         ui.button('Account').classes('bg-white text-blue')

js_code = '''
async function connectMetaMask() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the connected account
        } catch (error) {
            console.error('User  denied account access:', error);
            return null; // Return null if access is denied
        }15
    } else {
        console.log('MetaMask is not installed. Please install it to use this app.');
        return null; // Return null if MetaMask is not installed
    }
}
'''

def MetaMaskConnect():
	account = ui.run_javascript(f'''
	{js_code}
        connectMetaMask();
	''')
	if account:
		ui.notify(f'Connecting')
	else:
		ui.notify('Failed to connect to MetaMask.')
# --- Landing Page ---
@ui.page('/',  reconnect_timeout = 5000)
async def private_page():
    await ui.context.client.connected()
    HM = HeaderModule()
    NB = NavBar()
    NB.Accounts.on("click", lambda: ui.navigate.to('/LogInPage'))
    # --- Hero Section ---
    with ui.row().classes('items-center q-pa-xl bg-blue-100 rounded-lg shadow-md fade-in w-full'):
        with ui.column().classes('q-gutter-md'):
            ui.label('Revolutionizing Vaccine Logistics with IoT and Blockchain Security').classes('text-4xl font-bold text-blue-900')
            ui.label('Soltrack ensures safe, tamper-proof delivery of temperature-sensitive vaccines — from factory to facility.').classes('text-lg text-blue-800')
            with ui.row().classes('q-gutter-sm'):
                ui.button('Learn More', on_click=lambda: ui.notify('Scroll down to learn more.')).classes('bg-blue-700 text-white')
                ui.button('Get Started', on_click=lambda: ui.notify('Feature coming soon.')).classes('bg-white text-blue border border-blue-700')
        ui.image('Assets/IMG/banner.png').classes('rounded-lg shadow')

    # --- What is Soltrack? ---
    with ui.column().classes('q-pa-xl bg-white fade-in w-full'):
        ui.label('What is Soltrack?').classes('text-2xl font-semibold text-blue-900')
        ui.label('Soltrack is a smart logistics platform that uses IoT sensors and hybrid smart contracts to monitor and secure the delivery of temperature-sensitive vaccines.').classes('text-md text-gray-700')

    # --- Problem Section ---
    with ui.column().classes('q-pa-xl bg-blue-50 fade-in w-full'):
        ui.label('Why Soltrack Matters').classes('text-2xl font-semibold text-blue-900')
        with ui.row().classes('q-gutter-md'):
            for problem in [
                '🚫 Billions lost due to improper vaccine storage.',
                '🔍 Lack of trust and traceability in supply chains.',
                '⚠️ Manual monitoring is error-prone and tamperable.'
            ]:
                with ui.card().classes('p-4 w-full shadow-md bg-white'):
                    ui.label(problem).classes('text-gray-800')

    # --- Solution Section ---
    with ui.column().classes('q-pa-xl bg-white fade-in w-full'):
        ui.label('How Soltrack Works').classes('text-2xl font-semibold text-blue-900')
        with ui.row().classes('q-gutter-md'):
            for solution in [
                '📡 Sensor-Tracked Transport: Real-time temperature and route tracking.',
                '🔐 Smart Contract Escrow: Conditional release of funds.',
                '☁️ AWS & Chainlink: Secure, decentralized data integration.'
            ]:
                with ui.card().classes('p-4 w-full shadow-md bg-blue-50'):
                    ui.label(solution).classes('text-blue-900')

    # --- Features Section ---
    with ui.column().classes('q-pa-xl bg-blue-100 fade-in w-full'):
        ui.label('Features').classes('text-2xl font-semibold text-blue-900')
        with ui.row().classes('q-gutter-md'):
            features = [
                'Real-Time Temperature Monitoring',
                'Smart Contract Escrow System',
                'Tamper Alerts and Audit Logs',
                'Secure Blockchain Records',
                'AWS & Chainlink Integration',
                'Admin and Review Dashboard'
            ]
            for feature in features:
                with ui.card().classes('p-4 shadow-sm bg-white'):
                    ui.label(f'✅ {feature}').classes('text-gray-800')

    # --- Target Users ---
    with ui.column().classes('q-pa-xl bg-white fade-in w-full'):
        ui.label("Who It's For").classes('text-2xl font-semibold text-blue-900')
        for user in [
            '🏥 Vaccine Manufacturers',
            '🏥 Medical Distributors',
            '🏥 NGOs and Governments',
            '🏥 Cold Chain Logistics Providers'
        ]:
            ui.label(user).classes('text-md text-gray-700')

    # --- Demo CTA ---
    with ui.column().classes('items-center q-pa-xl bg-blue-50 text-center fade-in w-full'):
        ui.label('Try Our Demo').classes('text-2xl font-semibold text-blue-900')
        ui.button('View Contract Deployment', on_click=lambda: ui.notify('Demo not available yet.')).classes('bg-blue-700 text-white')

    FooterModule()

# --- Login ---
@ui.page('/LogInPage',  reconnect_timeout = 5000)
async def private_page():
    await ui.context.client.connected()
    HM = HeaderModule()
    HM
    LM = LogInModule()
    LM.LogInBtn.on("click", lambda: ui.navigate.to('/MMPage'))

@ui.page('/MMPage', reconnect_timeout=5000)
async def private_page():
    await ui.context.client.connected()

    ui.page_title("SolTrack | MetaMask Connect")

    HeaderModule()  # Inject the navigation/header

    with ui.row().style('width: 100%; height: 100vh;').classes("justify-center items-center bg-blue-50"):
        with ui.card().classes('p-8 shadow-lg bg-white rounded-xl w-96'):
            ui.label("MetaMask Connect").classes("text-2xl font-semibold text-blue-900 mb-4 text-center")

            # MetaMask Connect Button
            with ui.button(on_click=MetaMaskConnect).classes(
                "flex items-center justify-center bg-orange-400 text-white w-full py-2 rounded hover:bg-orange-500 mb-4"
            ):
                ui.image("Assets/IMG/MetaMask.png").classes('w-6 h-6 mr-2')
                ui.label("Connect with MetaMask").classes("text-md")

            # Continue Button
            ui.button("Continue", on_click=lambda: ui.navigate.to('/MainPage')) \
                .classes("bg-blue-700 text-white w-full hover:bg-blue-800")
            
@ui.page('/MainPage',  reconnect_timeout = 5000)
async def private_page():
    await ui.context.client.connected() 
    ui.page_title("SolTrackMain")
   # install_solc("0.5.16")

    HeaderModule()
    # NavBar()
    MainModule()
    # FooterModule()
            
# --- Footer ---
# with ui.footer().classes('bg-blue-900 text-white text-center p-6'):
#     ui.label('© 2025 Soltrack. All rights reserved.')
#     with ui.row().classes('justify-center '):
#         ui.link('GitHub', 'https://github.com/').classes('text-white hover:underline')
#         ui.link('Contact Us', '#').classes('text-white hover:underline')

ui.run(port = 8081, native = True)

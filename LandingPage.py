import os
from nicegui import ui
from HeaderModule import HeaderModule
from LogInModule import LogInModule
from MMModule import MMModule
from MainModule import MainModule
from FooterModule import FooterModule
from NavBar import NavBar
from solcx import compile_source, compile_standard, install_solc, get_installable_solc_versions

# Enhanced styling with modern CSS
ui.page_title('Soltrack | Smarter Vaccine Logistics')
ui.add_head_html('<link rel="preconnect" href="https://fonts.googleapis.com">')
ui.add_head_html('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap">')
ui.add_head_html('''
<style>
    body { 
        font-family: "Inter", sans-serif; 
        transition: all 0.3s ease-in-out;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0;
        padding: 0;
    }
    
    .hero-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        position: relative;
        overflow: hidden;
    }
    
    .hero-gradient::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 50%, rgba(255,255,255,0.1) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .feature-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid rgba(99, 102, 241, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #6366f1, transparent);
        transition: left 0.5s ease;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.2);
        border-color: #6366f1;
    }
    
    .pulse-dot {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.7; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .floating-animation {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .fade-in-up {
        opacity: 0;
        transform: translateY(30px);
        animation: fadeInUp 0.8s ease forwards;
    }
    
    .fade-in-left {
        opacity: 0;
        transform: translateX(-30px);
        animation: fadeInLeft 0.8s ease forwards;
    }
    
    .fade-in-right {
        opacity: 0;
        transform: translateX(30px);
        animation: fadeInRight 0.8s ease forwards;
    }
    
    @keyframes fadeInUp {
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInLeft {
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes fadeInRight {
        to { opacity: 1; transform: translateX(0); }
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border: none;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .btn-primary::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .btn-primary:hover::before {
        left: 100%;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.4);
    }
    
    .section-spacing {
        animation-delay: 0.2s;
    }
    
    .metric-card {
        background: linear-gradient(145deg, #1e293b, #334155);
        color: white;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
</style>
''')

js_code = '''
async function connectMetaMask() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0];
        } catch (error) {
            console.error('User denied account access:', error);
            return null;
        }
    } else {
        console.log('MetaMask is not installed. Please install it to use this app.');
        return null;
    }
}
'''

def MetaMaskConnect():
    account = ui.run_javascript(f'''
    {js_code}
    connectMetaMask();
    ''')
    if account:
        ui.notify(f'Connecting', type='positive')
    else:
        ui.notify('Failed to connect to MetaMask.', type='negative')

@ui.page('/', reconnect_timeout=5000)
async def private_page():
    await ui.context.client.connected()
    
    HM = HeaderModule()
    NB = NavBar()
    NB.Accounts.on("click", lambda: ui.navigate.to('/LogInPage'))
    
    # Hero Section with Glass Morphism
    with ui.row().classes('hero-gradient items-center justify-center min-h-screen w-full px-8 py-16'):
        with ui.column().classes('max-w-6xl w-full'):
            with ui.row().classes('items-center w-full gap-12'):
                # Left Content
                with ui.column().classes('flex-1 fade-in-left'):
                    with ui.row().classes('items-center mb-4'):
                        ui.element('div').classes('w-3 h-3 bg-green-400 rounded-full pulse-dot mr-3')
                        ui.label('Live Vaccine Tracking').classes('text-white/80 text-sm font-medium')
                    
                    ui.label('Revolutionizing Vaccine Logistics').classes('text-6xl font-bold text-blue mb-4 leading-tight')
                    ui.label('with IoT & Blockchain Security').classes('text-6xl font-bold bg-gradient-to-r from-yellow-300 to-pink-300 bg-clip-text text-transparent mb-6 leading-tight')
                    
                    ui.label('Soltrack ensures safe, tamper-proof delivery of temperature-sensitive vaccines — from factory to facility with real-time monitoring and smart contract automation.').classes('text-xl text-white/90 mb-8 leading-relaxed')
                    
                    # CTA Buttons
                    with ui.row().classes('gap-4'):
                        ui.button('🚀 Get Started', on_click=lambda: ui.navigate.to('/MMPage')).classes('btn-primary text-white px-8 py-4 text-lg font-semibold rounded-xl')
                        ui.button('📖 Learn More', on_click=lambda: ui.run_javascript('document.querySelector(".features-section").scrollIntoView({behavior: "smooth"})')).classes('glass-card text-white px-8 py-4 text-lg font-semibold rounded-xl border-2 border-white/30 hover:bg-white/10')
                
                # Right Content - Floating Image
                with ui.column().classes('flex-1 fade-in-right'):
                    ui.image('Assets/IMG/banner.png').classes('w-full max-w-lg floating-animation rounded-2xl shadow-2xl')

    # Stats Section
    with ui.row().classes('w-full bg-slate-900 py-16 px-8 justify-center'):
        with ui.row().classes('max-w-4xl gap-8'):
            stats = [
                ('$2.3B+', 'Lost Annually Due to Cold Chain Failures'),
                ('25%', 'Vaccines Damaged During Transport'),
                ('100%', 'Transparency with Blockchain'),
                ('24/7', 'Real-time Monitoring')
            ]
            for value, label in stats:
                with ui.card().classes('metric-card p-6 text-center flex-1 rounded-xl fade-in-up'):
                    ui.label(value).classes('text-3xl font-bold text-yellow-400 mb-2')
                    ui.label(label).classes('text-white/80 text-sm')

    # Problem Section
    with ui.row().classes('w-full bg-gradient-to-br from-red-50 to-orange-50 py-20 px-8 justify-center'):
        with ui.column().classes('max-w-6xl fade-in-up section-spacing'):
            ui.label('The Cold Chain Crisis').classes('text-4xl font-bold text-slate-800 text-center mb-4')
            ui.label('Billions of dollars worth of vaccines are wasted annually due to temperature breaches and lack of transparency').classes('text-xl text-slate-600 text-center mb-12')
            
            with ui.row().classes('gap-6'):
                problems = [
                    ('🔥', 'Temperature Breaches', 'Vaccines lose potency when exposed to improper temperatures', 'from-red-400 to-red-600'),
                    ('🔍', 'Lack of Traceability', 'No real-time visibility into vaccine condition and location', 'from-orange-400 to-orange-600'),
                    ('⚠️', 'Manual Monitoring', 'Error-prone human processes lead to costly mistakes', 'from-yellow-400 to-yellow-600')
                ]
                
                for icon, title, desc, gradient in problems:
                    with ui.card().classes(f'feature-card p-8 flex-1 rounded-2xl'):
                        ui.label(icon).classes('text-4xl mb-4')
                        ui.label(title).classes('text-xl font-bold text-slate-800 mb-3')
                        ui.label(desc).classes('text-slate-600 leading-relaxed')

    # Solution Section
    with ui.row().classes('w-full bg-gradient-to-br from-blue-50 to-indigo-100 py-20 px-8 justify-center features-section'):
        with ui.column().classes('max-w-6xl fade-in-up'):
            ui.label('How Soltrack Solves This').classes('text-4xl font-bold text-slate-800 text-center mb-4')
            ui.label('Advanced IoT sensors, blockchain security, and smart contracts working together').classes('text-xl text-slate-600 text-center mb-12')
            
            with ui.row().classes('gap-6'):
                solutions = [
                    ('📡', 'IoT Sensor Network', 'Real-time temperature, humidity, and location tracking with instant alerts'),
                    ('🔐', 'Smart Contract Escrow', 'Automated payment release based on delivery conditions'),
                    ('☁️', 'Hybrid Architecture', 'AWS cloud integration with Chainlink oracles for maximum reliability')
                ]
                
                for icon, title, desc in solutions:
                    with ui.card().classes('feature-card p-8 flex-1 rounded-2xl'):
                        ui.label(icon).classes('text-4xl mb-4')
                        ui.label(title).classes('text-xl font-bold text-blue-900 mb-3')
                        ui.label(desc).classes('text-slate-600 leading-relaxed')

    # Features Grid
    with ui.row().classes('w-full bg-white py-20 px-8 justify-center'):
        with ui.column().classes('max-w-6xl fade-in-up'):
            ui.label('Comprehensive Feature Set').classes('text-4xl font-bold text-slate-800 text-center mb-12')
            
            with ui.row().classes('gap-6 flex-wrap'):
                features = [
                    ('🌡️', 'Real-Time Monitoring', 'Continuous temperature and environmental tracking'),
                    ('💰', 'Smart Escrow', 'Conditional payment release system'),
                    ('🚨', 'Instant Alerts', 'Immediate notifications for any breaches'),
                    ('🔗', 'Blockchain Records', 'Immutable audit trail for compliance'),
                    ('🌐', 'Global Integration', 'AWS and Chainlink connectivity'),
                    ('📊', 'Admin Dashboard', 'Comprehensive management interface')
                ]
                
                for icon, title, desc in features:
                    with ui.card().classes('feature-card p-6 w-80 rounded-2xl'):
                        ui.label(icon).classes('text-3xl mb-3')
                        ui.label(title).classes('text-lg font-semibold text-slate-800 mb-2')
                        ui.label(desc).classes('text-slate-600 text-sm')

    # Target Users
    with ui.row().classes('w-full bg-gradient-to-br from-purple-50 to-pink-50 py-20 px-8 justify-center'):
        with ui.column().classes('max-w-4xl text-center fade-in-up'):
            ui.label('Built for Healthcare Leaders').classes('text-4xl font-bold text-slate-800 mb-12')
            
            with ui.row().classes('gap-8 justify-center'):
                users = [
                    ('🏭', 'Vaccine Manufacturers'),
                    ('🚚', 'Medical Distributors'),
                    ('🏛️', 'NGOs & Governments'),
                    ('❄️', 'Cold Chain Providers')
                ]
                
                for icon, title in users:
                    with ui.card().classes('feature-card p-6 w-48 rounded-2xl text-center'):
                        ui.label(icon).classes('text-4xl mb-3')
                        ui.label(title).classes('text-lg font-semibold text-slate-800')

    # Demo CTA Section
    with ui.row().classes('w-full bg-gradient-to-r from-indigo-600 to-purple-600 py-20 px-8 justify-center'):
        with ui.column().classes('max-w-4xl text-center fade-in-up'):
            ui.label('Ready to Transform Your Cold Chain?').classes('text-4xl font-bold text-white mb-6')
            ui.label('See how Soltrack can secure your vaccine logistics with cutting-edge technology').classes('text-xl text-white/90 mb-8')
            
            with ui.row().classes('gap-4 justify-center'):
                ui.button('🔗 Connect MetaMask', on_click=lambda: ui.navigate.to('/MMPage')).classes('btn-primary text-white px-8 py-4 text-lg font-semibold rounded-xl')
                ui.button('📱 View Demo', on_click=lambda: ui.navigate.to('/MainPage')).classes('glass-card text-white px-8 py-4 text-lg font-semibold rounded-xl border-2 border-white/30 hover:bg-white/10')

    FooterModule()

# Login Page
@ui.page('/LogInPage', reconnect_timeout=5000)
async def private_page():
    await ui.context.client.connected()
    HM = HeaderModule()
    LM = LogInModule()
    LM.LogInBtn.on("click", lambda: LM.LogIn(LM.Name.value, LM.Pass.value))

# MetaMask Connection Page
@ui.page('/MMPage', reconnect_timeout=5000)
async def private_page():
    await ui.context.client.connected()
    ui.page_title("SolTrack | MetaMask Connect")
    HeaderModule()

    with ui.row().style('width: 100%; height: 100vh;').classes("justify-center items-center hero-gradient"):
        with ui.card().classes('glass-card p-12 rounded-3xl w-96 text-center'):
            ui.label("🦊 Connect to Web3").classes("text-3xl font-bold text-white mb-6")
            ui.label("Connect your MetaMask wallet to access Soltrack's blockchain features").classes("text-white/80 mb-8")

            with ui.button(on_click=MetaMaskConnect).classes(
                "flex items-center justify-center bg-gradient-to-r from-orange-400 to-orange-500 text-white w-full py-4 rounded-xl hover:from-orange-500 hover:to-orange-600 mb-6 transition-all"
            ):
                ui.image("Assets/IMG/MetaMask.png").classes('w-8 h-8 mr-3')
                ui.label("Connect with MetaMask").classes("text-lg font-semibold")

            ui.button("Continue to Dashboard", on_click=lambda: ui.navigate.to('/MainPage')) \
                .classes("btn-primary w-full py-4 text-lg font-semibold rounded-xl")

# Main Application Page
@ui.page('/MainPage', reconnect_timeout=5000)
async def private_page():
    await ui.context.client.connected()
    ui.page_title("SolTrack | Dashboard")
    HeaderModule()
    MainModule()

ui.run(
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8080))
)
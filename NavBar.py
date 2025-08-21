import os
from nicegui import ui

class NavBar:
    def __init__(self):
        # Add modern CSS styling
        ui.add_head_html('''
        <style>
            .modern-nav {
                background: rgba(255, 255, 255, 0.1) !important;
                backdrop-filter: blur(20px) !important;
                border-bottom: 1px solid rgba(255, 255, 255, 0.2) !important;
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            
            .logo-text {
                background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%) !important;
                -webkit-background-clip: text !important;
                -webkit-text-fill-color: transparent !important;
                background-clip: text !important;
                font-weight: 800 !important;
                letter-spacing: -0.02em !important;
                transition: all 0.3s ease !important;
            }
            
            .logo-text:hover {
                background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%) !important;
                -webkit-background-clip: text !important;
                -webkit-text-fill-color: transparent !important;
                background-clip: text !important;
                transform: scale(1.05);
            }
            
            .nav-link {
                color: rgba(255, 255, 255, 0.9) !important;
                text-decoration: none !important;
                padding: 0.5rem 1rem !important;
                border-radius: 0.5rem !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                position: relative !important;
                font-weight: 500 !important;
                overflow: hidden !important;
            }
            
            .nav-link::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
                transition: left 0.5s ease;
            }
            
            .nav-link:hover::before {
                left: 100%;
            }
            
            .nav-link:hover {
                color: white !important;
                background: rgba(255, 255, 255, 0.1) !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
            }
            
            .account-btn {
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
                border: none !important;
                color: white !important;
                padding: 0.75rem 1.5rem !important;
                border-radius: 0.75rem !important;
                font-weight: 600 !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                position: relative !important;
                overflow: hidden !important;
                box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.3) !important;
            }
            
            .account-btn::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
                transition: left 0.5s ease;
            }
            
            .account-btn:hover::before {
                left: 100%;
            }
            
            .account-btn:hover {
                background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
                transform: translateY(-2px) scale(1.02) !important;
                box-shadow: 0 8px 25px 0 rgba(99, 102, 241, 0.4) !important;
            }
            
            .nav-icon {
                margin-right: 0.5rem !important;
                transition: transform 0.3s ease !important;
            }
            
            .account-btn:hover .nav-icon {
                transform: rotate(360deg) !important;
            }
            
            .logo-container {
                display: flex !important;
                align-items: center !important;
                gap: 0.75rem !important;
            }
            
            .logo-icon {
                width: 2rem !important;
                height: 2rem !important;
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
                border-radius: 0.5rem !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                color: white !important;
                font-size: 1.25rem !important;
                font-weight: bold !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3) !important;
            }
            
            .logo-icon:hover {
                transform: rotate(10deg) scale(1.1) !important;
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4) !important;
            }
            
            .nav-container {
                max-width: 1200px !important;
                margin: 0 auto !important;
                width: 100% !important;
            }
            
            .mobile-menu-btn {
                display: none !important;
                color: white !important;
                background: rgba(255, 255, 255, 0.1) !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                border-radius: 0.5rem !important;
                padding: 0.5rem !important;
                transition: all 0.3s ease !important;
            }
            
            .mobile-menu-btn:hover {
                background: rgba(255, 255, 255, 0.2) !important;
            }
            
            @media (max-width: 768px) {
                .desktop-nav {
                    display: none !important;
                }
                .mobile-menu-btn {
                    display: flex !important;
                }
            }
            
            .status-indicator {
                width: 8px !important;
                height: 8px !important;
                background: #10b981 !important;
                border-radius: 50% !important;
                animation: pulse-green 2s infinite !important;
                margin-left: 0.5rem !important;
            }
            
            @keyframes pulse-green {
                0%, 100% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.7; transform: scale(1.2); }
            }
        </style>
        ''')
        
        # Modern Navigation Bar with Glass Morphism
        with ui.header().classes('modern-nav text-white p-4'):
            with ui.row().classes('nav-container items-center justify-between'):
                # Logo Section
                with ui.row().classes('logo-container items-center'):
                    # Logo Icon
                    with ui.element('div').classes('logo-icon'):
                        ui.label('S').classes('text-sm font-bold')
                    
                    # Logo Text with Status
                    with ui.row().classes('items-center'):
                        ui.label('Soltrack').classes('logo-text text-2xl')
                        ui.element('div').classes('status-indicator')
                
                # Desktop Navigation Links
                with ui.row().classes('desktop-nav items-center gap-2'):
                    # Navigation Links
                    nav_items = [
                        ('🏠', 'Home', '#'),
                        ('ℹ️', 'About', '#'),
                        ('⭐', 'Features', '#'),
                        ('🎮', 'Demo', '#')
                    ]
                    
                    for icon, text, link in nav_items:
                        with ui.link(link).classes('nav-link'):
                            ui.label(f'{icon} {text}').classes('text-sm')
                
                # Account Section
                with ui.row().classes('items-center gap-3'):
                    # Connection Status
                    with ui.row().classes('items-center'):
                        ui.element('div').classes('w-2 h-2 bg-green-400 rounded-full pulse-dot mr-2')
                        ui.label('Connected').classes('text-xs text-white/70 hidden md:block')
                    
                    # Account Button
                    self.Accounts = ui.button().classes('account-btn')
                    with self.Accounts:
                        ui.icon("account_circle").classes('nav-icon')
                        ui.label('Account').classes('text-sm font-semibold hidden sm:inline')
                
                # Mobile Menu Button
                with ui.button().classes('mobile-menu-btn md:hidden'):
                    ui.icon('menu')

ui.run(
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8080))
)
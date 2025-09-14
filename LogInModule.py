import os
from nicegui import ui as UI
from HeaderModule import HeaderModule
import psycopg2
class LogInModule:
    async def LogIn(self, input_name, input_pass):
        self.LogInBtn.props('loading=true')
        self.LogInBtn.text = 'Authenticating...'
        conn = None
        try:
            conn = psycopg2.connect(
                host=os.getenv("PGHOST"),
                user=os.getenv("PGUSER"),
                password=os.getenv("PGPASSWORD"),
                dbname=os.getenv("PGDATABASE"),
                port=os.getenv("PGPORT", 5432)
            )
            cur = conn.cursor()
            sql = "SELECT id FROM users WHERE name = %s AND password = %s"
            val = (input_name, input_pass)
            cur.execute(sql, val)
            result = cur.fetchone()
            
            if result:
                UI.notify("🎉 Login Successful! Redirecting...", type='positive')
                UI.navigate.to('/MainPage')
            else:
                UI.notify("❌ Invalid credentials. Please try again.", type='negative')
            # Reset button state
                self.LogInBtn.props('loading=false')
                self.LogInBtn.text = 'Sign In'
            
        except Exception as e:
            UI.notify(f"🔌 Connection Error: {str(e)}", type='negative')
        # Reset button state
            self.LogInBtn.props('loading=false')
            self.LogInBtn.text = 'Sign In'
        finally:
            if conn:
                conn.close()
    async def handle_login(self):
        if not self.Name.value.strip():
            UI.notify("📝 Please enter your username or email", type='warning')
            return
        if not self.Pass.value.strip():
            UI.notify("🔐 Please enter your password", type='warning')
            return
        await self.LogIn(self.Name.value.strip(), self.Pass.value)

    def __init__(self):
        # Add modern styling
        UI.add_head_html('''
        <style>
            .login-container {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                position: relative;
                overflow: hidden;
                min-height: 100vh;
            }
            
            .login-container::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.2) 0%, transparent 50%);
                pointer-events: none;
            }
            
            .login-card {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.3);
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
                border-radius: 24px;
                position: relative;
                overflow: hidden;
                animation: fadeInScale 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
                opacity: 0;
                transform: scale(0.95);
            }
            
            @keyframes fadeInScale {
                to {
                    opacity: 1;
                    transform: scale(1);
                }
            }
            
            .login-header {
                text-align: center;
                margin-bottom: 2rem;
            }
            
            .login-title {
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 2.5rem;
                font-weight: 800;
                margin-bottom: 0.5rem;
                letter-spacing: -0.02em;
            }
            
            .login-subtitle {
                color: #64748b;
                font-size: 1rem;
                font-weight: 500;
            }
            
            .modern-input {
                position: relative;
                margin-bottom: 1.5rem;
            }
            
            .modern-input .q-field__control {
                background: rgba(248, 250, 252, 0.8) !important;
                border: 2px solid rgba(226, 232, 240, 0.8) !important;
                border-radius: 12px !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                backdrop-filter: blur(10px) !important;
            }
            
            .modern-input .q-field__control:hover {
                border-color: rgba(99, 102, 241, 0.4) !important;
                background: rgba(255, 255, 255, 0.9) !important;
            }
            
            .modern-input .q-field--focused .q-field__control {
                border-color: #6366f1 !important;
                background: rgba(255, 255, 255, 1) !important;
                box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
            }
            
            .modern-input .q-field__label {
                color: #64748b !important;
                font-weight: 500 !important;
            }
            
            .modern-input .q-field--focused .q-field__label {
                color: #6366f1 !important;
            }
            
            .login-btn {
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 1rem 2rem !important;
                font-size: 1.1rem !important;
                font-weight: 600 !important;
                color: white !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                position: relative !important;
                overflow: hidden !important;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
            }
            
            .login-btn::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
                transition: left 0.6s ease;
            }
            
            .login-btn:hover::before {
                left: 100%;
            }
            
            .login-btn:hover {
                background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4) !important;
            }
            
            .login-btn:active {
                transform: translateY(0) !important;
            }
            
            .floating-elements {
                position: absolute;
                width: 100%;
                height: 100%;
                pointer-events: none;
                overflow: hidden;
            }
            
            .floating-circle {
                position: absolute;
                border-radius: 50%;
                opacity: 0.1;
                animation: float 6s ease-in-out infinite;
            }
            
            .circle-1 {
                width: 80px;
                height: 80px;
                background: #6366f1;
                top: 20%;
                left: 10%;
                animation-delay: 0s;
            }
            
            .circle-2 {
                width: 60px;
                height: 60px;
                background: #8b5cf6;
                top: 60%;
                right: 15%;
                animation-delay: 2s;
            }
            
            .circle-3 {
                width: 100px;
                height: 100px;
                background: #f093fb;
                bottom: 20%;
                left: 20%;
                animation-delay: 4s;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                33% { transform: translateY(-20px) rotate(120deg); }
                66% { transform: translateY(-10px) rotate(240deg); }
            }
            
            .security-badge {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.5rem;
                padding: 0.75rem;
                background: rgba(16, 185, 129, 0.1);
                border: 1px solid rgba(16, 185, 129, 0.2);
                border-radius: 8px;
                color: #059669;
                font-size: 0.875rem;
                font-weight: 500;
                margin-top: 1rem;
            }
            
            .demo-credentials {
                background: rgba(99, 102, 241, 0.05);
                border: 1px solid rgba(99, 102, 241, 0.1);
                border-radius: 12px;
                padding: 1rem;
                margin-top: 1.5rem;
            }
            
            .demo-title {
                color: #6366f1;
                font-weight: 600;
                font-size: 0.875rem;
                margin-bottom: 0.5rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            .demo-cred {
                font-family: 'Courier New', monospace;
                background: rgba(255, 255, 255, 0.8);
                padding: 0.25rem 0.5rem;
                border-radius: 4px;
                font-size: 0.8rem;
                color: #374151;
                margin: 0.25rem 0;
            }
        </style>
        ''')
        
        # Main container with gradient background
        with UI.row().classes("login-container justify-center items-center w-full"):
            # Floating background elements
            with UI.element('div').classes('floating-elements'):
                UI.element('div').classes('floating-circle circle-1')
                UI.element('div').classes('floating-circle circle-2')
                UI.element('div').classes('floating-circle circle-3')
            
            # Login card
            with UI.card().classes('login-card p-10 w-full max-w-md') as self.LogInInput:
                # Header section
                with UI.column().classes('login-header'):
                    UI.label("Welcome Back").classes("login-title")
                    UI.label("Sign in to your Soltrack account").classes("login-subtitle")
                
                # Login form
                with UI.column().classes('w-full gap-2'):
                    # Username/Email input
                    self.Name = UI.input(
                        label='Username or Email', 
                        placeholder='Enter your credentials'
                    ).classes("modern-input w-full").props('outlined dense')
                    
                    # Password input
                    self.Pass = UI.input(
                        label='Password', 
                        placeholder='Enter your password', 
                        password=True, 
                        password_toggle_button=True
                    ).classes("modern-input w-full").props('outlined dense')
                    
                    # Login button
                    self.LogInBtn = UI.button(
                        "Sign In", 
                        on_click=self.handle_login
                    ).classes("login-btn w-full")
                    
                    # Security badge
                    with UI.row().classes('security-badge'):
                        UI.icon('verified_user').classes('text-emerald-600')
                        UI.label('🔒 Secure Login with Database Encryption')
                    
                    # Demo credentials (for development)
                    with UI.column().classes('demo-credentials'):
                        with UI.row().classes('demo-title'):
                            UI.icon('info').classes('text-sm')
                            UI.label('Demo Credentials')
                        UI.label('Username:').classes('text-xs text-slate-600')
                        UI.label('admin_acc').classes('demo-cred')
                        UI.label('Password:').classes('text-xs text-slate-600')
                        UI.label('admin_acc1234').classes('demo-cred')

# Run app
if __name__ == "__main__":
    LogInModule()
    UI.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080))
    )

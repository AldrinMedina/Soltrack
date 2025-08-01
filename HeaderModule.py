from nicegui import ui 


class HeaderModule:
    def __init__(self):
        ui.add_css('''
        .Link {
            color: white;
            text-decoration: none;
        }
        .Link:hover {
            color: yellow;
            cursor: pointer;
        }
        ''')
        
        ui.page_title('Soltrack | Smarter Vaccine Logistics')
        ui.add_head_html('<link rel="preconnect" href="https://fonts.googleapis.com">')
        ui.add_head_html('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap">')
        ui.add_head_html('''
        <style>
            body { font-family: "Inter", sans-serif; transition: all 0.3s ease-in-out; }
            .fade-in { opacity: 0; transform: translateY(20px); animation: fadeInUp 0.6s ease forwards; }
            @keyframes fadeInUp { to { opacity: 1; transform: none; } }
        </style>
        ''')
ui.run()

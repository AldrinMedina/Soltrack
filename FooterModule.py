import os
from nicegui import ui 


class FooterModule:
    def __init__(self):
        # --- Footer ---
        with ui.footer().classes('bg-blue-900 text-white text-center p-6'):
            ui.label('© 2025 Soltrack. All rights reserved.')
            with ui.row().classes('justify-center'):
                ui.link('GitHub', 'https://github.com/').classes('text-white hover:underline')
                ui.link('Contact Us', '#').classes('text-white hover:underline')


ui.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080))
    )

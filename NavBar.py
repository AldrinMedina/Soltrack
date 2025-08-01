from nicegui import ui 


class NavBar:
    def __init__(self):
        # --- Navigation Bar ---
        with ui.header().classes('bg-blue-900 text-white p-4 shadow-md justify-between'):
            with ui.row().classes('items-center'):
                ui.label('Soltrack').classes('text-xl font-bold')
            with ui.row().classes('q-gutter-md items-center'):
                ui.link('Home', '#').classes('text-white hover:underline')
                ui.link('About', '#').classes('text-white hover:underline')
                ui.link('Features', '#').classes('text-white hover:underline')
                ui.link('Demo', '#').classes('text-white hover:underline')
                self.Accounts = ui.button('Account').classes('bg-white text-blue')
                with self.Accounts:
                    ui.icon("account_circle")

ui.run()
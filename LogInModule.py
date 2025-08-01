from nicegui import ui as UI
from HeaderModule import HeaderModule
class LogInModule:
    def __init__(self):
        # Wrapper row to center the login card
        with UI.row().style('width: 100%; height: 100vh;').classes("justify-center items-center bg-blue-100"):
            with UI.card().classes('p-8 shadow-lg bg-white rounded-lg w-96') as self.LogInInput:
                UI.label("Log In").classes("text-2xl font-semibold text-blue-900 mb-4")

                UI.input(label='Username or Email', placeholder='Enter your credentials') \
                    .classes("w-full mb-4")

                UI.input(label='Password', placeholder='Enter your password', password=True, password_toggle_button=True) \
                    .classes("w-full mb-6")

                self.LogInBtn = UI.button("Confirm", on_click=lambda: UI.notify("Logging in...")) \
                    .classes("bg-blue-700 text-white w-full hover:bg-blue-800")

UI.run()
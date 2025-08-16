import os
from nicegui import ui as UI
from HeaderModule import HeaderModule
import pymysql


class LogInModule:

    async def LogIn(self, input_name, input_pass):
        try:
            mydb = pymysql.connect(
                host=os.getenv("MYSQLHOST"),
                user=os.getenv("MYSQLUSER"),
                password=os.getenv("MYSQLPASSWORD"),
                database=os.getenv("MYSQLDATABASE"),
                port=int(os.getenv("MYSQLPORT", 3306)),
                cursorclass=pymysql.cursors.DictCursor
            )
            mycursor = mydb.cursor()

            sql = "SELECT id FROM users WHERE name = %s AND password = %s"
            val = (input_name, input_pass)
            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            if result:
                UI.notify("Logging In")
                UI.navigate.to('/MainPage')
            else:
                UI.notify("Wrong username or password")
        except Exception as e:
            UI.notify(f"Database error: {e}")

    async def handle_login(self):
        await self.LogIn(self.Name.value, self.Pass.value)

    def __init__(self):
        with UI.row().style('width: 100%; height: 100vh;').classes("justify-center items-center bg-blue-100"):
            with UI.card().classes('p-8 shadow-lg bg-white rounded-lg w-96') as self.LogInInput:
                UI.label("Log In").classes("text-2xl font-semibold text-blue-900 mb-4")
                self.Name = UI.input(label='Username or Email', placeholder='Enter your credentials').classes("w-full mb-4")
                self.Pass = UI.input(label='Password', placeholder='Enter your password', password=True, password_toggle_button=True).classes("w-full mb-6")
                self.LogInBtn = UI.button("Confirm", on_click=self.handle_login).classes("bg-blue-700 text-white w-full hover:bg-blue-800")

# Run app
LogInModule()
UI.run(
	host="0.0.0.0",
    port=int(os.getenv("PORT", 8080))
)

from nicegui import ui as UI
from HeaderModule import HeaderModule
import mysql.connector


class LogInModule:

	async def LogIn(self, input_name, input_pass):
		mydb = mysql.connector.connect(
		    host=os.getenv("MYSQLHOST"),
		    user=os.getenv("MYSQLUSER"),
		    password=os.getenv("MYSQLPASSWORD"),
		    database=os.getenv("MYSQLDATABASE"),
		    port=int(os.getenv("MYSQLPORT", 3306))
		)
		mycursor = mydb.cursor()
		#if input_name == "Joseph M.":
		#	if input_pass == "12345":
		#		UI.notify("Logging In")
		#		UI.navigate.to('/MainPage')
		#	else:
		#		UI.notify("Wrong password.")
		#else:
		#	UI.notify("No account found.")
		

		sql = "SELECT Id FROM Credentials WHERE Name = %s AND Password = %s"
		val = (input_name, input_pass)
		mycursor.execute(sql, val)
		result = mycursor.fetchall()
		if result:
			UI.notify("Logging In")
			UI.navigate.to('/MainPage')
		else:
			UI.notify ("Wrong password/email")
	def __init__(self):
	
		with UI.row().style('width: 100%; height: 100vh;').classes("justify-center items-center bg-blue-100"):
			with UI.card().classes('p-8 shadow-lg bg-white rounded-lg w-96') as self.LogInInput:
				UI.label("Log In").classes("text-2xl font-semibold text-blue-900 mb-4")
				self.Name = UI.input(label='Username or Email', placeholder='Enter your credentials').classes("w-full mb-4")
				self.Pass= UI.input(label='Password', placeholder='Enter your password', password=True, password_toggle_button=True).classes("w-full mb-6")
				self.LogInBtn = UI.button("Confirm", on_click=lambda: LogIn(Name.value, Pass.value)).classes("bg-blue-700 text-white w-full hover:bg-blue-800")

UI.run()

from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
import sqlite3
root = Tk()
root.geometry("300x260")
root.resizable(0,0)

db_name = '/home/allan/docs/python/python_com_primo/desafio_primo/primo_uri.db'

menu = Menu(root)
root.config(menu=menu)

sv1 = StringVar()
sv2 = StringVar()
def run_query(query, parameters=()):
	print(query)
	print(parameters)
	with sqlite3.connect(db_name) as conn:
		cursor = conn.cursor()
		result = cursor.execute(query, parameters)

		conn.commit()
	return result

def salvar_cadastro():
	query = """INSERT INTO subscribers (name,email) VALUES (?, ?);"""
	parameters = (sv1.get(),sv2.get())
	
	query_select = """SELECT name FROM subscribers;"""
	rows = run_query(query_select)
	for row in rows:
		# print(len(row[0]))
		if row[0] == sv1.get():
			print(row)
		elif len(row[0]) > 45:
			print("Tamanho execido.")
		else:
			run_query(query,parameters)
	sv1.set("")
	sv2.set("")

def subs_cadastrar():
	print('oi')

	## name
	FrameSubsCad = Frame(width=300,height=260)
	FrameSubsCad.place(x=0,y=0)
	nameLabel = Label(FrameSubsCad, text="Name:")
	nameLabel.place(x=20,y=40)
	emailEntry = Entry(FrameSubsCad, width=25,textvariable=sv1)
	emailEntry.place(x=63,y=40)
	## email
	emailLabel = Label(FrameSubsCad, text="Email:")
	emailLabel.place(x=20,y=60)
	emailEntry = Entry(FrameSubsCad, width=25,textvariable=sv2)
	emailEntry.place(x=63,y=60)

	#Button
	saveButton = Button(FrameSubsCad,text="Salvar", width=10,command=salvar_cadastro)
	saveButton.place(x=170,y=220)
	# nameEntry.pack(ipadx = )
	



## menu news
news_menu = Menu(menu)
subscribe_menu = Menu(menu)
menu.add_cascade(label="News", menu=news_menu)
news_menu.add_command(label="Listar")
news_menu.add_separator()
news_menu.add_command(label="Cadastrar")
## menu subsccribe
menu.add_cascade(label="Subscribes", menu=subscribe_menu)
subscribe_menu.add_command(label="Listar")
subscribe_menu.add_separator()
subscribe_menu.add_command(label="Cadastrar", command=subs_cadastrar)




root.mainloop()

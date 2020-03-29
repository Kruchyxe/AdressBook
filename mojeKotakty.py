from tkinter import *
import sqlite3
import dodajOsoby
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


def funcDodajOsoby():
	addpage = dodajOsoby.DodajOsoby()


class MojeKontakty(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("650x650+620+200")
		self.title("Moje kontakty")
		self.resizable(False, False)

		# Ramka
		self.top = Frame(self, height=150, bg='white')
		self.top.pack(fill=X)
		self.bottomFrame = Frame(self, height=500, bg="#EB0165")
		self.bottomFrame.pack(fill=X)

		# Nagłowek, obrazek oraz data
		self.top_image = PhotoImage(file='Ikony/person_icon.png')
		self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
		self.top_image_lbl.place(x=120, y=10)
		self.naglowek = Label(self.top, text=" Moje kontakty", font='calibre 15 bold',
		                      fg='#4B0082', bg='white')
		self.naglowek.place(x=260, y=60)

		# PasekPrzew //ScrollBar//
		self.pasekPrz = Scrollbar(self.bottomFrame, orient=VERTICAL)

		# Lista //listbox
		self.lista = Listbox(self.bottomFrame, width=50, height=31)
		self.lista.grid(row=0, column=0, padx=(40, 0))
		self.pasekPrz.config(command=self.lista.yview)
		self.lista.config(yscrollcommand=self.pasekPrz.set)
		self.pasekPrz.grid(row=0, column=1, sticky=N + S)

		osoby = cur.execute("SELECT * FROM osoby").fetchall()
		# print(osoby)
		count = 0
		for osoba in osoby:
			self.lista.insert(count, str(osoba[0]) + "-" + osoba[1] + " " + osoba[2])
			count += 1

		# Przyciski Dodaj Aktualizuj Pokaż Usuń //Buttons Add Update Display Delete
		przyciskDodaj = Button(self.bottomFrame, text='Dodaj', width=12, font='calibre 12 italic',
		                       bg='#EDFA8E', command=self.funcdodajOsoby)
		przyciskDodaj.grid(row=0, column=2, sticky=N, padx=5, pady=5)

		przyciskAktualny = Button(self.bottomFrame, text='Aktualizuj', width=12,
		                          font='calibre 12 italic', bg='#EDFA8E',
		                          command=self.funcUpdateOsoba)
		przyciskAktualny.grid(row=0, column=2, sticky=N, padx=5, pady=45)

		przyciskPokaz = Button(self.bottomFrame, text='Pokaż', width=12, font='calibre 12 italic',
		                       bg='#EDFA8E', command=self.funcPokazKontakty)
		przyciskPokaz.grid(row=0, column=2, sticky=N, padx=5, pady=85)

		przyciskUsun = Button(self.bottomFrame, text='Usuń', width=12, font='calibre 12 italic',
		                      bg='#EDFA8E', command=self.funcUsunOsobe)
		przyciskUsun.grid(row=0, column=2, sticky=N, padx=5, pady=125)

	def funcdodajOsoby(self):
		dodajstrone = dodajOsoby.DodajOsoby()
		self.destroy()

	def funcUpdateOsoba(self):
		global osoba_id
		selected_item = self.lista.curselection()
		osoba = self.lista.get(selected_item)
		osoba_id = osoba.split("-")[0]
		aktualizuj = Update()

	def funcPokazKontakty(self):
		global osoba_id
		selected_item = self.lista.curselection()
		osoba = self.lista.get(selected_item)
		osoba_id = osoba.split('-')[0]
		pokaz = Pokaz()
		self.destroy()

	def funcUsunOsobe(self):
		selected_item = self.lista.curselection()
		osoba = self.lista.get(selected_item)
		osoba_id = osoba.split("-")[0]

		mbox = messagebox.askquestion("Uwaga", "Czy jesteś pewien że chcesz usunąć kontakt?")

		if mbox == 'yes':
			try:
				cur.execute("DELETE FROM osoby WHERE osoby_id=?", (osoba_id))
				con.commit()
				messagebox.showinfo("Ok", "Kontakt został usuniety")
				self.destroy()

			except:
				messagebox.showinfo("Info", "Kontakt nie został usunięty")


class Update(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("650x750+550+200")
		self.title("Aktualizacja danych osobowych")
		self.resizable(False, False)

		# uzyskanie id z bazy danych
		global osoba_id

		osoba = cur.execute("SELECT * FROM osoby WHERE osoby_id =?", (osoba_id,))
		osoba_info = osoba.fetchall()
		print(osoba_info)
		self.osoba_id = osoba_info[0][0]
		self.osoba_imie = osoba_info[0][1]
		self.osoba_nazwisko = osoba_info[0][2]
		self.osoba_email = osoba_info[0][3]
		self.osoba_phone = osoba_info[0][4]
		self.osoba_address = osoba_info[0][5]

		# Ramka
		self.top = Frame(self, height=150, bg='white')
		self.top.pack(fill=X)
		self.bottomFrame = Frame(self, height=600, bg="#EB0165")
		self.bottomFrame.pack(fill=X)

		# Nagłowek, obrazek
		self.top_image = PhotoImage(file='Ikony/addperson.png')
		self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
		self.top_image_lbl.place(x=120, y=10)
		self.naglowek = Label(self.top, text=" Aktualizuj dane osobowe", font='calibre 15 bold',
		                      fg='#4B0082', bg='white')
		self.naglowek.place(x=260, y=60)

		###########################################################

		# Labels and entries
		# Imię // name
		self.lbl_imie = Label(self.bottomFrame, text='Imię        ',
		                      font='calibre 12 bold', fg='white',
		                      bg='#EB0165')
		self.lbl_imie.place(x=40, y=40)
		self.ent_imie = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_imie.insert(0, self.osoba_imie)
		self.ent_imie.place(x=150, y=45)

		# Nazwisko // Surname
		self.lbl_nazwisko = Label(self.bottomFrame, text='Nazwisko',
		                          font='calibre 12 bold', fg='white',
		                          bg='#EB0165')
		self.lbl_nazwisko.place(x=40, y=80)
		self.ent_nazwisko = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_nazwisko.insert(0, self.osoba_nazwisko)
		self.ent_nazwisko.place(x=150, y=85)

		# adres email // email
		self.lbl_email = Label(self.bottomFrame, text='Email      ',
		                       font='calibre 12 bold', fg='white',
		                       bg='#EB0165')
		self.lbl_email.place(x=40, y=120)
		self.ent_email = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_email.insert(0, self.osoba_email)
		self.ent_email.place(x=150, y=125)

		# numer komórkowy // mobile number
		self.lbl_phone = Label(self.bottomFrame, text='Telefon   ',
		                       font='calibre 12 bold', fg='white',
		                       bg='#EB0165')
		self.lbl_phone.place(x=40, y=160)
		self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_phone.insert(0, self.osoba_phone)
		self.ent_phone.place(x=150, y=165)

		# Adres // Adress
		self.lbl_address = Label(self.bottomFrame, text='Address ', font='calibre 12 bold',
		                         fg='white', bg='#EB0165')
		self.lbl_address.place(x=40, y=300)
		self.address = Text(self.bottomFrame, width=31, height=15, wrap=WORD)
		self.address.insert('1.0', self.osoba_address)
		self.address.place(x=150, y=200)

		# Przycisk
		button = Button(self.bottomFrame, text='Aktualizuj dane', command=self.updateOsoba)
		button.place(x=270, y=465)
		self.lift()

	def updateOsoba(self):
		osoba_id = self.osoba_id
		osoba_imie = self.ent_imie.get()
		osoba_nazwisko = self.ent_nazwisko.get()
		osoba_email = self.ent_email.get()
		osoba_phone = self.ent_phone.get()
		osoba_address = self.address.get(1.0, 'end-1c')

		try:
			query = "UPDATE osoby set osoby_imie =?, osoby_nazwisko =?, osoby_email =?, osoby_phone =?, " \
			        "osoby_address =? WHERE osoby_id =? "
			cur.execute(query, (osoba_imie, osoba_nazwisko, osoba_email, osoba_phone, osoba_address, osoba_id))
			con.commit()
			messagebox.showinfo(title="Info", message="Dane osoby zostały zaktualizowane pomyślnie")
			self.destroy()

		except:
			messagebox.showwarning(title="Uwaga", message="Dane osoby nie mogły zostać zaktualizowane")


class Pokaz(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry('650x750+550+200')
		self.title('Pokaz kontakty')
		self.resizable(False, False)

		# uzyskanie id z bazy danych
		global osoba_id

		osoba = cur.execute("SELECT * FROM osoby WHERE osoby_id =?", (osoba_id,))
		osoba_info = osoba.fetchall()
		print(osoba_info)
		self.osoba_id = osoba_info[0][0]
		self.osoba_imie = osoba_info[0][1]
		self.osoba_nazwisko = osoba_info[0][2]
		self.osoba_email = osoba_info[0][3]
		self.osoba_phone = osoba_info[0][4]
		self.osoba_address = osoba_info[0][5]

		# Ramka
		self.top = Frame(self, height=150, bg='white')
		self.top.pack(fill=X)
		self.bottomFrame = Frame(self, height=600, bg="#EB0165")
		self.bottomFrame.pack(fill=X)

		# Nagłowek, obrazek
		self.top_image = PhotoImage(file='Ikony/addperson.png')
		self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
		self.top_image_lbl.place(x=120, y=10)
		self.naglowek = Label(self.top, text=" Kontakt", font='calibre 15 bold',
		                      fg='#4B0082', bg='white')
		self.naglowek.place(x=260, y=60)

		###########################################################

		# Labels and entries
		# Imię // name
		self.lbl_imie = Label(self.bottomFrame, text='Imię        ',
		                      font='calibre 12 bold', fg='white',
		                      bg='#EB0165')
		self.lbl_imie.place(x=40, y=40)
		self.ent_imie = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_imie.insert(0, self.osoba_imie)
		self.ent_imie.config(state='disabled')
		self.ent_imie.place(x=150, y=45)

		# Nazwisko // Surname
		self.lbl_nazwisko = Label(self.bottomFrame, text='Nazwisko',
		                          font='calibre 12 bold', fg='white',
		                          bg='#EB0165')
		self.lbl_nazwisko.place(x=40, y=80)
		self.ent_nazwisko = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_nazwisko.insert(0, self.osoba_nazwisko)
		self.ent_nazwisko.config(state='disabled')
		self.ent_nazwisko.place(x=150, y=85)

		# adres email // email
		self.lbl_email = Label(self.bottomFrame, text='Email      ',
		                       font='calibre 12 bold', fg='white',
		                       bg='#EB0165')
		self.lbl_email.place(x=40, y=120)
		self.ent_email = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_email.insert(0, self.osoba_email)
		self.ent_email.config(state='disabled')
		self.ent_email.place(x=150, y=125)

		# numer komórkowy // mobile number
		self.lbl_phone = Label(self.bottomFrame, text='Telefon   ',
		                       font='calibre 12 bold', fg='white',
		                       bg='#EB0165')
		self.lbl_phone.place(x=40, y=160)
		self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_phone.insert(0, self.osoba_phone)
		self.ent_phone.config(state='disabled')
		self.ent_phone.place(x=150, y=165)

		# Adres // Adress
		self.lbl_address = Label(self.bottomFrame, text='Address ', font='calibre 12 bold',
		                         fg='white', bg='#EB0165')
		self.lbl_address.place(x=40, y=300)
		self.address = Text(self.bottomFrame, width=31, height=15, wrap=WORD)
		self.address.insert('1.0', self.osoba_address)
		self.address.config(state='disabled')
		self.address.place(x=150, y=200)

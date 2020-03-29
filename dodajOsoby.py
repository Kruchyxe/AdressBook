from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class DodajOsoby(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("650x750+550+200")
		self.title("Dodaj osoby")
		self.resizable(False, False)

		# Ramka
		self.top = Frame(self, height=150, bg='white')
		self.top.pack(fill=X)
		self.bottomFrame = Frame(self, height=600, bg="#EB0165")
		self.bottomFrame.pack(fill=X)

		# Nagłowek, obrazek
		self.top_image = PhotoImage(file='Ikony/addperson.png')
		self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
		self.top_image_lbl.place(x=120, y=10)
		self.naglowek = Label(self.top, text=" Moi znajomi", font='calibre 15 bold',
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
		self.ent_imie.insert(0, 'Podaj swoje imię ')
		self.ent_imie.place(x=150, y=45)

		# Nazwisko // Surname
		self.lbl_nazwisko = Label(self.bottomFrame, text='Nazwisko',
		                          font='calibre 12 bold', fg='white',
		                          bg='#EB0165')
		self.lbl_nazwisko.place(x=40, y=80)
		self.ent_nazwisko = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_nazwisko.insert(0, 'Podaj swoje nazwisko ')
		self.ent_nazwisko.place(x=150, y=85)

		# adres email // email
		self.lbl_email = Label(self.bottomFrame, text='Email      ',
		                       font='calibre 12 bold', fg='white',
		                       bg='#EB0165')
		self.lbl_email.place(x=40, y=120)
		self.ent_email = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_email.insert(0, 'Podaj swój email ')
		self.ent_email.place(x=150, y=125)

		# numer komórkowy // mobile number
		self.lbl_phone = Label(self.bottomFrame, text='Telefon   ',
		                       font='calibre 12 bold', fg='white',
		                       bg='#EB0165')
		self.lbl_phone.place(x=40, y=160)
		self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
		self.ent_phone.insert(0, 'Podaj swój numer telefonu ')
		self.ent_phone.place(x=150, y=165)

		# Adres // Adress
		self.lbl_address = Label(self.bottomFrame, text='Address ', font='calibre 12 bold',
		                         fg='white', bg='#EB0165')
		self.lbl_address.place(x=40, y=300)
		self.address = Text(self.bottomFrame, width=31, height=15, wrap=WORD)
		self.address.place(x=150, y=200)

		# Przycisk
		button = Button(self.bottomFrame, text='Dodaj osobę', command=self.dodajosobe)
		button.place(x=270, y=465)
		self.lift()

	def dodajosobe(self):
		imie = self.ent_imie.get()
		nazwisko = self.ent_nazwisko.get()
		email = self.ent_email.get()
		phone = self.ent_phone.get()
		address = self.address.get(1.0, 'end-1c')

		if (imie and nazwisko and email and phone and address != ""):
			try:
				query = "INSERT INTO 'osoby' (osoby_imie,osoby_nazwisko,osoby_email,osoby_phone,osoby_address) VALUES(?,?,?,?,?)"
				cur.execute(query, (imie, nazwisko, email, phone, address))
				con.commit()
				messagebox.showinfo("Sukces", "Poprawnie wprowadzono dane do bazy danych", icon='info')

			except:
				messagebox.showerror('Błąd', "Nie można dodać do bazy danych", icon='warning')

		else:
			messagebox.showerror('Błąd', "Pola nie mogą być puste", icon='warning')

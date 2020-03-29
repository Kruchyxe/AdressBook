from tkinter import *
import mojeKotakty, dodajOsoby, infoOmnie
import datetime

date = datetime.datetime.now().date()


class Aplikacja(object):
	def __init__(self, master):
		self.master = master

		# Ramka
		self.top = Frame(master, height=150, bg='white')
		self.top.pack(fill=X)
		self.bottom = Frame(master, height=500, bg="#CDEBA7")
		self.bottom.pack(fill=X)

		# Nagłowek, obrazek oraz data
		self.top_image = PhotoImage(file='Ikony/book.png')
		self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
		self.top_image_lbl.place(x=120, y=10)
		self.naglowek = Label(self.top, text="Moja ksiązka adresowa", font='calibre 15 bold',
		                      fg='#4B0082', bg='white')
		self.naglowek.place(x=260, y=60)
		self.data_lbl = Label(self.top, text="Data " + str(date), font='calibre 12 bold',
		                      bg='white', fg='#4B0082')
		self.data_lbl.place(x=450, y=5)

		# Przycisk_1 //first button//
		self.btn1Icon = PhotoImage(file='Ikony/man.png')
		self.personBtn = Button(self.bottom, text=' Moje kontakty ', font='calibre 12 italic',
		                        bg='#F5F5DC', command=self.openMojeKontakty)
		self.personBtn.config(image=self.btn1Icon, compound=LEFT)
		self.personBtn.place(x=250, y=10)

		# Przycisk 2 //second button//
		self.btn2Icon = PhotoImage(file='Ikony/add.png')
		self.addpersonBtn = Button(self.bottom, text=' Dodaj osoby    ',
		                        font='calibre 12 italic',
		                        bg='#F5F5DC', command=self.funcDodajOsoby)
		self.addpersonBtn.config(image=self.btn2Icon, compound=LEFT)
		self.addpersonBtn.place(x=250, y=70)

		# Przycisk 3 //third button
		self.btn3Icon = PhotoImage(file='Ikony/info.png')
		self.aboutBtn = Button(self.bottom, text='  O mnie           ', font='calibre 12 italic',
		                        bg='#F5F5DC', command = infoOmnie.main)
		self.aboutBtn.config(image=self.btn3Icon, compound=LEFT)
		self.aboutBtn.place(x=250, y=130)

	def openMojeKontakty(self):
		kontakty = mojeKotakty.MojeKontakty()

	def funcDodajOsoby(self):
		dodajosobyokno = dodajOsoby.DodajOsoby()


def main():
	root = Tk()
	app = Aplikacja(root)
	root.title("Książka Adresowa")
	root.geometry("650x550+352+200")
	root.resizable(False, False)
	root.mainloop()


if __name__ == "__main__":
	main()

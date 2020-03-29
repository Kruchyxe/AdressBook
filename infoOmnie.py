from tkinter import *


class InfoOmnie:
	def __init__(self, root):
		self.root = root

		ramka = Frame(root, bg='#ffa500', width=550, height=550)
		ramka.pack(fill=BOTH)
		text = Label(ramka, text='Informacje o mnie.'
		        '\n Ta strona stworzona została na podstawie materiałów '
		            '\nszkoleniowych UDEMY'
		        '\n dzieki temu powstał mój pierwszy program okienkowy ;)',
		             font='calibre 12 bold', bg='#ffa500', fg='white')
		text.place(x=20, y=70)


def main():
	root = Tk()
	app = InfoOmnie(root)
	root.title(" Informacje o mnie")
	root.geometry("550x550+550+200")
	root.resizable(False, False)
	root.mainloop()


if __name__ == '__main__':
	main()

import wikipedia
import webbrowser
import tkinter as tk
import random

def yes1(page):
	page_open = wikipedia.page(page)
	webbrowser.open(page_open.url)

def wiki():
	page = wikipedia.random(1)
	var = "Do you wanna read about "+page+" ?"
	label = tk.Label(root, text=var, fg='red', font = ('calibri',10))
	label.place(relx=0.4,rely=0.3)
	yes = tk.Button(root, text='Yes', command = lambda:yes1(page) ,font = ('calibri',10))
	yes.place(relx=0.4,rely=0.5, relheight=0.2, relwidth=0.2)
	no = tk.Button(root, text='No', command = wiki ,font = ('calibri',10))
	no.place(relx=0.4,rely=0.7, relheight=0.2, relwidth=0.2)
root = tk.Tk()
root.title('Random wikipedia')

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

frame = tk.Frame(root, bg='#595959', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

random = tk.Button(frame, text='Random', command = wiki ,font = ('calibri',10))
random.place(relx=0.25,rely=0.2, relheight=0.7, relwidth=0.5)



root.mainloop()

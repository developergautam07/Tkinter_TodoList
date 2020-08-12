from tkinter import *
window = Tk()
window.title("TODO-LIST")

cont = Listbox(window, font="Georgia 24 bold",bg="Silver")
tas = StringVar()
user_in = Entry(window, font="Georgia 24", textvariable=tas, bg="pink")
add_fun = lambda content=cont, task=tas: content.insert(END,task.get())
del_fun = lambda content=cont : content.delete(ANCHOR)
btn_add = Button(window, text="Add", font="Arial 20", command=add_fun, bg="Green", fg="White", padx=20)
btn_del = Button(window, text="Delete", font="Arial 20", command=del_fun, bg="Red", fg="White")

cont.grid(row = 0, column = 0, columnspan = 2, padx=5, pady=10)
user_in.grid(row = 1,column = 0, columnspan=2, padx=5, pady=10)
btn_add.grid(row = 2,column = 0)
btn_del.grid(row = 2,column = 1)
window.mainloop()

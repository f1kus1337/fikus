from tkinter import *

#поля

def pole():
    root3 = Toplevel()
    root3.title("Пятнашки")

    button = Button(root3, text="Выход", command=root3.destroy)
    button.pack()
    root3.mainloop()

#игра на мвремя

def time():
    root2 = Toplevel()
    root2.title("Пятнашки")

    button = Button(root2, text="Выход", command=root2.destroy)
    button.pack()
    root2.mainloop()

#пятнашки сама игра

def open_2115():
    root = Toplevel()
    root.title("Пятнашки")
    root.mainloop()


root = Tk()
root.title("Пятнашки")
root.geometry("450x300")


def menu():
    top1 = Toplevel(root)
    top1.title("Пятнашки")
    top1.geometry("450x300")

    label = Label(top1, text="Выбор режима:")
    label.pack()

    button1 = Button(top1, text="Обычный режим", command=open_2115)
    button1.pack()

    button2 = Button(top1, text="Игра на время", command=time)
    button2.pack()

    button3 = Button(top1, text="Пользователь вводит размеры поля", command=pole)
    button3.pack()

    top1.mainloop()

button = Button(root, text="ИГРАТЬ", command=menu)
button.pack(anchor="center", expand=1)
button.place(x=200, y=80)


root.mainloop()

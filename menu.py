import random
from tkinter import *
import tkinter as tk
from tkinter import Tk, Button, Label, messagebox

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Пятнашки")
        self.root.geometry(f"{550}x{400}+{500}+{200}")

        # Создаем сетку 4x4
        self.grid = []
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.root, width=6, height=3, bg='white', fg='black')
                btn.grid(row=i, column=j, sticky="nsew")
                row.append(btn)
            self.grid.append(row)

        # Кнопка "Назад" для возврата в меню
        back_button = Button(self.root, text="Назад", command=self.back_to_menu, width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white")
        back_button.grid(row=4, column=0, columnspan=4, pady=10)

        # Заполняем сетку числами из списка numbers или пустыми ячейками
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
        random.shuffle(numbers)

        for i in range(4):
            for j in range(4):
                self.grid[i][j]["text"] = numbers.pop(0)

        # Привязываем обработчик события для каждой кнопки в сетке
        for row in self.grid:
            for btn in row:
                btn.bind("<Button-1>", self.move)

    def back_to_menu(self):
        self.root.destroy()
        main_menu()

    def is_solved(self):
        solved_list = list(range(1, 16)) + [0]
        grid_values = []
        for row in self.grid:
            for btn in row:
                grid_values.append(int(btn["text"]) if btn["text"] != '' else 0)
        return grid_values == solved_list

    def move(self, event):
        clicked_btn = event.widget
        clicked_row, clicked_col = None, None

        # Find the position of the clicked button in the grid
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == clicked_btn:
                    clicked_row = i
                    clicked_col = j
                    break

        # Move the button if possible
        if clicked_row > 0 and self.grid[clicked_row - 1][clicked_col]["text"] == '':
            self.grid[clicked_row - 1][clicked_col]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''  # up
        elif clicked_row < 3 and self.grid[clicked_row + 1][clicked_col]["text"] == '':
            self.grid[clicked_row + 1][clicked_col]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''  # down
        elif clicked_col > 0 and self.grid[clicked_row][clicked_col - 1]["text"] == '':
            self.grid[clicked_row][clicked_col - 1]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''  # left
        elif clicked_col < 3 and self.grid[clicked_row][clicked_col + 1]["text"] == '':
            self.grid[clicked_row][clicked_col + 1]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''  # right

        if self.is_solved():
            self.show_win_popup()

    def show_win_popup(self):
        win_popup = tk.Toplevel(self.root)
        win_popup.title("Поздравляем, вы выиграли!")
        win_popup.geometry(f"{550}x{400}+{500}+{200}")

        message_label = tk.Label(win_popup, text="Поздравляем, вы выиграли!", font=("Helvetica", 12, "bold"))
        message_label.pack(pady=20)

        back_button = tk.Button(win_popup, text="Назад", command=self.back_to_menu, font=("Helvetica", 9, "bold"),
                                fg="black", bg="white")
        back_button.pack(pady=10)

        exit_button = tk.Button(win_popup, text="Выход", command=self.root.quit, font=("Helvetica", 9, "bold"),
                                fg="black", bg="white")
        exit_button.pack(pady=10)


def main_menu():
    root = Tk()
    root.title("Пятнашки")
    root.geometry(f"{550}x{400}+{500}+{200}")

    Label(root, text="Выбор режима:", font=("Helvetica", 12, "bold"), fg="black").pack(pady=10)

    Button(root, text="Обычный режим", command=lambda: start_game(root), width=45, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
    Button(root, text="На время", command=lambda: time_game(root), width=45, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
    Button(root, text="Пользователь вводит размеры игрового поля", command=lambda: usergame(root), width=45, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
    Button(root, text="Правила", command=lambda: rules(root), width=45, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
    Button(root, text="Выход", command=root.destroy, width=45, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)

    root.mainloop()

def start_game(root):
    root.destroy()
    new_root = Tk()
    Game(new_root)
    new_root.mainloop()

def time_game(root):
    root.destroy()
    new_root = Tk()
    TimedGame(new_root)
    new_root.mainloop()

class TimedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Пятнашки")
        self.root.geometry("550x450+500+200")

        self.time_selection_frame = tk.Frame(self.root)
        self.time_selection_frame.pack(pady=10)

        tk.Button(self.time_selection_frame, text='1 минута', command=lambda: self.start_game(60), width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
        tk.Button(self.time_selection_frame, text='2 минуты', command=lambda: self.start_game(120), width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
        tk.Button(self.time_selection_frame, text='3 минуты', command=lambda: self.start_game(180), width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)
        Button(self.root, text="Назад", command=self.back_to_menu, width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)

    def back_to_menu(self):
        self.root.destroy()
        main_menu()

    def start_game(self, time_seconds):
        self.time_left = time_seconds
        self.time_selection_frame.pack_forget()
        self.setup_game()
        self.update_timer()

    def setup_game(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(side="top", pady=20)

        self.timer_label = tk.Label(self.root, text='', font=("Helvetica", 16))
        self.timer_label.pack(side="top")

        self.grid = []
        numbers = list(range(1, 16)) + ['']
        random.shuffle(numbers)

        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.game_frame, text='', width=6, height=3, bg='white', fg='black')
                btn.grid(row=i, column=j, sticky="nsew")
                btn["text"] = str(numbers.pop(0))
                row.append(btn)
            self.grid.append(row)

        for row in self.grid:
            for btn in row:
                btn.bind("<Button-1>", self.move)

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label['text'] = f'Времени осталось: {self.time_left // 60}:{self.time_left % 60:02d}'
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.game_frame.pack_forget()
            self.timer_label['text'] = 'Время вышло!'
            tk.Button(self.root, text='Новая игра', command=self.reset_game).pack(side="top")

    def reset_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

    def is_solved(self):
        solved_list = list(range(1, 16)) + [0]
        grid_values = []
        for row in self.grid:
            for btn in row:
                grid_values.append(int(btn["text"]) if btn["text"] != '' else 0)
        return grid_values == solved_list

    def move(self, event):
        clicked_btn = event.widget
        clicked_row, clicked_col = None, None

        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == clicked_btn:
                    clicked_row = i
                    clicked_col = j
                    break

        if clicked_row > 0 and self.grid[clicked_row - 1][clicked_col]["text"] == '':
            self.grid[clicked_row - 1][clicked_col]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''
        elif clicked_row < 3 and self.grid[clicked_row + 1][clicked_col]["text"] == '':
            self.grid[clicked_row + 1][clicked_col]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''
        elif clicked_col > 0 and self.grid[clicked_row][clicked_col - 1]["text"] == '':
            self.grid[clicked_row][clicked_col - 1]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''
        elif clicked_col < 3 and self.grid[clicked_row][clicked_col + 1]["text"] == '':
            self.grid[clicked_row][clicked_col + 1]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''

        if self.is_solved():
            self.show_win_popup()

    def show_win_popup(self):
        win_popup = tk.Toplevel(self.root)
        win_popup.title("Поздравляем, вы выиграли!")
        win_popup.geometry(f"{550}x{400}+{500}+{200}")

        message_label = tk.Label(win_popup, text="Поздравляем, вы выиграли!", font=("Helvetica", 12, "bold"))
        message_label.pack(pady=20)

        back_button = tk.Button(win_popup, text="Назад", command=self.back_to_menu, font=("Helvetica", 9, "bold"),
                                fg="black", bg="white")
        back_button.pack(pady=10)

        exit_button = tk.Button(win_popup, text="Выход", command=self.root.quit, font=("Helvetica", 9, "bold"),
                                fg="black", bg="white")
        exit_button.pack(pady=10)

def usergame(root):
    root.destroy()
    new_root = Tk()
    UserSizeGame(new_root)
    new_root.mainloop()

class UserSizeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Пятнашки")
        self.root.geometry(f"{550}x{400}+{500}+{200}")

        self.size_label = Label(self.root, text="Введите размер поля (NxN):", font=("Helvetica", 12, "bold"))
        self.size_label.pack(pady=10)

        self.size_entry = Entry(self.root, font=("Helvetica", 12), width=5)
        self.size_entry.pack(pady=5)

        self.start_button = Button(self.root, text="Начать игру", command=self.start_game, width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white")
        self.start_button.pack(pady=5)

        Button(self.root, text="Назад", command=self.back_to_menu, width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=5)

    def back_to_menu(self):
        self.root.destroy()
        main_menu()

    def start_game(self):
        try:
            size = int(self.size_entry.get())
            if size < 2:
                raise ValueError
            self.root.destroy()
            self.play_game(size)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное значение размера поля (целое число, большее 1).")

    def play_game(self, size):
        new_root = Tk()
        new_root.title("Пятнашки")
        new_root.geometry(f"{550 + 50 * (size - 4)}x{400 + 50 * (size - 4)}+{500}+{200}")
        GameCustomSize(new_root, size)
        new_root.mainloop()

class GameCustomSize:
    def __init__(self, root, size):
        self.root = root
        self.size = size
        self.grid = []

        for i in range(size):
            row = []
            for j in range(size):
                btn = tk.Button(self.root, width=6, height=3, bg='white', fg='black')
                btn.grid(row=i, column=j, sticky="nsew")
                row.append(btn)
            self.grid.append(row)

        back_button = Button(self.root, text="Назад", command=self.back_to_menu, width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white")
        back_button.grid(row=size, column=0, columnspan=size, pady=10)

        numbers = list(range(1, size*size)) + ['']
        random.shuffle(numbers)

        for i in range(size):
            for j in range(size):
                self.grid[i][j]["text"] = numbers.pop(0)

        for row in self.grid:
            for btn in row:
                btn.bind("<Button-1>", self.move)

    def back_to_menu(self):
        self.root.destroy()
        main_menu()

    def is_solved(self):
        solved_list = list(range(1, self.size*self.size)) + [0]
        grid_values = []
        for row in self.grid:
            for btn in row:
                grid_values.append(int(btn["text"]) if btn["text"] != '' else 0)
        return grid_values == solved_list

    def move(self, event):
        clicked_btn = event.widget
        clicked_row, clicked_col = None, None

        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == clicked_btn:
                    clicked_row = i
                    clicked_col = j
                    break

        if clicked_row > 0 and self.grid[clicked_row - 1][clicked_col]["text"] == '':
            self.grid[clicked_row - 1][clicked_col]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''
        elif clicked_row < self.size - 1 and self.grid[clicked_row + 1][clicked_col]["text"] == '':
            self.grid[clicked_row + 1][clicked_col]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''
        elif clicked_col > 0 and self.grid[clicked_row][clicked_col - 1]["text"] == '':
            self.grid[clicked_row][clicked_col - 1]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''
        elif clicked_col < self.size - 1 and self.grid[clicked_row][clicked_col + 1]["text"] == '':
            self.grid[clicked_row][clicked_col + 1]["text"] = self.grid[clicked_row][clicked_col]["text"]
            self.grid[clicked_row][clicked_col]["text"] = ''

        if self.is_solved():
            self.show_win_popup()

    def show_win_popup(self):
        win_popup = tk.Toplevel(self.root)
        win_popup.title("Поздравляем, вы выиграли!")
        win_popup.geometry(f"{550}x{400}+{500}+{200}")

        message_label = tk.Label(win_popup, text="Поздравляем, вы выиграли!", font=("Helvetica", 12, "bold"))
        message_label.pack(pady=20)

        back_button = tk.Button(win_popup, text="Назад", command=self.back_to_menu, font=("Helvetica", 9, "bold"),
                                fg="black", bg="white")
        back_button.pack(pady=10)

        exit_button = tk.Button(win_popup, text="Выход", command=self.root.quit, font=("Helvetica", 9, "bold"),
                                fg="black", bg="white")
        exit_button.pack(pady=10)


def rules(rule):

    rule = Tk()
    rule.title("Пятнашки")

    rule.configure()
    rule.geometry(f"{550}x{400}+{500}+{200}")


    rrule = Label(rule, text="Правила:", bg="white", fg="black", font=("Comic Sans MS", 12, "bold"))
    rrule.pack()

    rulesss = """Цель игры заключается в упорядочивания чисел от 1 до 15 на игровом поле размером 4x4, перемещая их по полю с помощью пустой ячейки.

    В приложении имеется три режима игры:

    В режиме "Обычный" пользователь будет перемещать числа на игровом поле, используя свободную ячейку, с целью упорядочить их по возрастанию.
    -----------------------------------------------------------------
    В режиме "На время" пользователь будет играть с ограниченным временем. Задача остается такой же - упорядочить числа. У пользователя будет отведено определенное время для решения головоломки, и он должен постараться сделать это как можно быстрее.
    -----------------------------------------------------------------
    В режиме "Пользователь вводит размеры поля" пользователь будет иметь возможность настроить размеры игрового поля и уровень сложности самостоятельно. Например, пользователь может выбрать поле с размерами 3x3 или 5x5, изменить количество чисел на поле и т.д. Задача пользователя всё равно остается той же - упорядочить числа на поле.

                   """
    ruletext = tk.Text(rule, wrap="word")

    ruletext.insert("1.0", rulesss)

    ruletext.pack()
    ruletext.configure(bg="white", fg="black", font=("Comic Sans MS", 10, "bold"))

    Button(rule, text="Назад", command=lambda: back_to_menu(new_root), width=20, height=1, font=("Helvetica", 9, "bold"), fg="black", bg="white").pack(pady=10)

def back_to_menu(root):
    root.destroy()
    main_menu()

main_menu()

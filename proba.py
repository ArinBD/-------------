import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename
from random import randint

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Результат", f"Сумма: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")

def calculate_vchet():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        messagebox.showinfo("Результат", f"Вычетание: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")

def calculate_umn():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        messagebox.showinfo("Результат", f"Произведение: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")

def calculate_step():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 ** num2
        messagebox.showinfo("Результат", f"Степень: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")

def calculate_del():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2
        messagebox.showinfo("Результат", f"Деление: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")

def calculate_del_non():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 // num2
        messagebox.showinfo("Результат", f"Деление: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")

def calculate_del_ost():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 % num2
        messagebox.showinfo("Результат", f"Деление: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите другое число.")


def wrt():
    a = [randint(0,101) for x in range(10)]
    filename=askopenfilename()
    file=open(filename, "w")
    file.write(str(a))
    file.close()

def rd():
   filename=askopenfilename()
   file=open(filename, "r")
   nums = file.read()
   numsArray = list(map(int,nums.strip("[]").split(", ")))
   s=sum(numsArray)/ len(numsArray)
   messagebox.showinfo("результат", f"{s}")

def switch_frame(frame):
    frame.tkraise()

def ran():
    a = [randint(0,101) for x in range(10)]
    b= max(a)
    d= min(a)
    c= sorted(a)
    c_revers = sorted(a,reverse=True)
    S = 0
    for i in a:
     S += i

def min():
    a = [randint(0,101) for x in range(10)]
    f= min(a)
    messagebox.showinfo("результат", f"{a, f}")


def max():
    a = [randint(0,101) for x in range(10)]
    b= max(a)
    messagebox.showinfo("результат", f"{a, b}")

def sort():
    a = [randint(0,101) for x in range(10)]
    d= sorted(a)
    messagebox.showinfo("результат", f"{a, d}")

def sort_revers():
    a = [randint(0,101) for x in range(10)]
    c= sorted(a,reverse=True)
    messagebox.showinfo("результат", f"{a, c}")


root = tk.Tk()
root.title("Laba6")
root.geometry("500x400")


frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky='news')


# меню
tk.Label(frame1, text="Меню", font=("Arial Bold", 30)).pack()
tk.Button(frame1, text="Калькулятор", font=("Arial", 14), bg='dark green',fg="white", command=lambda: switch_frame(frame2)).pack()
tk.Button(frame1, text="Работа с файлами", font=("Arial", 14), bg='dark green',fg="white",command=lambda: switch_frame(frame3)).pack()
tk.Button(frame1, text="Рандомайзер", font=("Arial", 14), bg='dark green',fg="white",command=lambda: switch_frame(frame4)).pack()



#калькулятор
tk.Label(frame2, text="Число 1:").pack()
entry1 = tk.Entry(frame2)
entry1.pack()
tk.Label(frame2, text="Число 2:").pack()
entry2 = tk.Entry(frame2)
entry2.pack()
tk.Button(frame2, text="Сумма",font=("Arial", 14), bg='dark green',fg="white", command=calculate_sum).pack()
tk.Button(frame2, text="Вычитание",font=("Arial", 14), bg='dark green',fg="white", command=calculate_vchet).pack()
tk.Button(frame2, text="Умножение",font=("Arial", 14), bg='dark green',fg="white", command=calculate_umn).pack()
tk.Button(frame2, text="Степень",font=("Arial", 14), bg='dark green',fg="white", command=calculate_step).pack()
tk.Button(frame2, text="Деление",font=("Arial", 14), bg='dark green',fg="white", command=calculate_del).pack()
tk.Button(frame2, text="Деление без остатка",font=("Arial", 14), bg='dark green',fg="white", command=calculate_del_non).pack()
tk.Button(frame2, text="Остаток деления",font=("Arial", 14), bg='dark green',fg="white", command=calculate_del_ost).pack()
tk.Button(frame2, text="Вернутся в меню",font=("Arial", 14), bg='dark green',fg="white", command=lambda: switch_frame(frame1)).pack()

#рандомайзер
tk.Button(frame4, text="Минимальное число",font=("Arial", 14), bg='dark green',fg="white", command=min).pack()
tk.Button(frame4, text="Максимальное число",font=("Arial", 14), bg='dark green',fg="white", command=max).pack()
tk.Button(frame4, text="Сортировка по возрастанию",font=("Arial", 14), bg='dark green',fg="white", command=sort).pack()
tk.Button(frame4, text="Сортировка по убыванию",font=("Arial", 14), bg='dark green',fg="white", command=sort_revers).pack()

tk.Button(frame4, text="Вернутся в меню",font=("Arial", 14), bg='dark green',fg="white", command=lambda: switch_frame(frame1)).pack()

#файлы
tk.Button(frame3, text="записать в выбранный файл",font=("Arial", 14), bg='dark green',fg="white", command=wrt).pack()
tk.Button(frame3, text="прочитать файл",font=("Arial", 14), bg='dark green',fg="white", command=rd).pack()

tk.Button(frame3, text="Вернутся в меню",font=("Arial", 14), bg='dark green',fg="white", command=lambda: switch_frame(frame1)).pack()

switch_frame(frame1)  # Start with frame 1
root.mainloop()
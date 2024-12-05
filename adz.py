#laba 2
#a = float(input("Введите первое число:"))
#b = float(input("Введите второе число:"))
#print("Сложение", a + b)
#print("Вычитание", a - b)
#print("Умножение", a * b)
#print("возвидение в степень", a ** b)
#if b == 0:
#   print("на ноль делить нельзя")
#else:
#   print("Деление без остатка", a // b)
#   print("Остаток деления", a % b)
#   print("Деление", a / b)

#laba3
#from random import randint
#a = [randint(0,101) for x in range(10)]
#print(a)
#b= max(a)
#print(b)
#d= min(a)
#print(d)
#c= sorted(a)
#print(c)
#c_revers = sorted(a,reverse=True)
#print(c_revers)
#S = 0
#for i in a:
#    S += i
#print(S)

#laba4
from random import randint
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filename=askopenfilename()

print("Если хотите прочитать файл нажмите 1")
print("Если хотите редактировать файл нвжмите 0")
с=int(input("Введите число:"))
a = [randint(0,101) for x in range(10)]
def wrt():
   file=open(filename, "w")
   file.write(str(a))
   file.close()

def rd():
   file=open(filename, "r")
   nums = file.read()
   numsArray = list(map(int,nums.strip("[]").split(", ")))
   s=sum(numsArray)/ len(numsArray)
   print(s)


if с == 0:
   wrt()
elif с == 1:
   rd()
else:
   print("Не верное число")
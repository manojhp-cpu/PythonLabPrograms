# part-B
# 6. Create a GUI using Tkinter module

from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Enter Number')
        self.lbl2 = Label(win, text='Result')

        self.t1 = Entry(win, bd=3)
        self.t2 = Entry(win)

        self.btn1 = Button(win, text='Find Factorial',
                           command=self.calculate_factorial)

        self.lbl1.place(x=120, y=50)
        self.t1.place(x=200, y=50)

        self.btn1.place(x=200, y=100)
        self.lbl2.place(x=160, y=150)
        self.t2.place(x=200, y=150)

    def calculate_factorial(self):
        fact = 1
        self.t2.delete(0, 'end')
        num = int(self.t1.get())
        for i in range(2, num + 1):
            fact *= i
        self.t2.insert(END, str(fact))


window = Tk()
mywin = MyWindow(window)
window.title('Factorial Program')
window.geometry("400x300")
window.mainloop()

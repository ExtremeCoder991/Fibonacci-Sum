# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:45:31 2022

@author: prave
"""

from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")
trubone = Entry(root).place(x = 137, y = 70)
label_series = Label(root, text="Fibonacci Series:  ")
label_series1 = Label(root, text="Fibonacci Sum:  ")



def Fibonacci():
    input_number = int(trubone.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0
    while (counter <= input_number):
        label_series["text"] += str(sum) + " "
        label_series["text"] = "Fibonnaci Sum : " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum

btn = Button(root, text="Show Fibonacci Series", command=Fibonacci) 


btn.pack()
label_series.pack()
label_series1.pack()
root.mainloop()


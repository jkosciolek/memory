from tkinter import *

selected = ""
buttons = []

"""
na poczatku tworzy dictionary, klucz to jeden obrazek, wartosc to drugi i przyporzadkowuje losowe niezajete pola

"""


def click_action(button):
    global selected
    if selected == "":
        selected = button['text']
    else:
        if button['text'] == selected:
            for i in range(16):
                if buttons[i]['text'] == selected:
                    buttons[i].config(state="disabled")
            selected = ""
        else:
            selected = ""


if __name__ == '__main__':
    root = Tk()
    root.title("Memory")
    root.geometry("1280x720")

    button1 = Button(root, text="a", width=10, height=10,  command=lambda: click_action(button1))
    button2 = Button(root, text="b", width=10, height=10, command=lambda: click_action(button2))
    button3 = Button(root, text="b", width=10, height=10, command=lambda: click_action(button3))
    button4 = Button(root, text="g", width=10, height=10, command=lambda: click_action(button4))
    button5 = Button(root, text="e", width=10, height=10, command=lambda: click_action(button5))
    button6 = Button(root, text="c", width=10, height=10, command=lambda: click_action(button6))
    button7 = Button(root, text="f", width=10, height=10, command=lambda: click_action(button7))
    button8 = Button(root, text="h", width=10, height=10, command=lambda: click_action(button8))
    button9 = Button(root, text="d", width=10, height=10, command=lambda: click_action(button9))
    button10 = Button(root, text="h", width=10, height=10, command=lambda: click_action(button10))
    button11 = Button(root, text="e", width=10, height=10, command=lambda: click_action(button11))
    button12 = Button(root, text="f", width=10, height=10, command=lambda: click_action(button12))
    button13 = Button(root, text="a", width=10, height=10, command=lambda: click_action(button13))
    button14 = Button(root, text="c", width=10, height=10, command=lambda: click_action(button14))
    button15 = Button(root, text="g", width=10, height=10, command=lambda: click_action(button15))
    button16 = Button(root, text="d", width=10, height=10, command=lambda: click_action(button16))
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    buttons.append(button4)
    buttons.append(button5)
    buttons.append(button6)
    buttons.append(button7)
    buttons.append(button8)
    buttons.append(button9)
    buttons.append(button10)
    buttons.append(button11)
    buttons.append(button12)
    buttons.append(button13)
    buttons.append(button14)
    buttons.append(button15)
    buttons.append(button16)


    button1.grid(row=0, column=0, columnspan=1)
    button2.grid(row=0, column=1, )
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=1, column=0)
    button6.grid(row=1, column=1)
    button7.grid(row=1, column=2)
    button8.grid(row=1, column=3)
    button9.grid(row=2, column=0)
    button10.grid(row=2, column=1)
    button11.grid(row=2, column=2)
    button12.grid(row=2, column=3)
    button13.grid(row=3, column=0)
    button14.grid(row=3, column=1)
    button15.grid(row=3, column=2)
    button16.grid(row=3, column=3)

    root.mainloop()

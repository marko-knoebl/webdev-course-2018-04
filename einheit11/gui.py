import Tkinter
import tkMessageBox
import random

secret = random.randint(1, 100)

def check_guess():
    if int(guess.get()) == secret:
        result_text = "CORRECT!"
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    tkMessageBox.showinfo('Result', result_text)

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Guess the secret number!")
guess = Tkinter.Entry(window)
submit = Tkinter.Button(window, text="Submit", command=check_guess)

for element in [greeting, guess, submit]:
    element.pack()

window.mainloop()
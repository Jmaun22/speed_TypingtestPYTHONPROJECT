
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import math




# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None









# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="speed.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)


# email_label = Label(text="Email/Username")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password")
# password_label.grid(row=3, column=0)

#Enteries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "jessemaun@gmail.com")
#
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)

#Buttons
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)

# search_button = Button(text="Search", width=13, command=find_password)
# search_button.grid(row=1, column=2)







# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If its the 1,3,5,7

    if reps % 8 == 0:
        # If its the 8th rep:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # if its 2nd/4th/ 6th
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"







# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")






# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="speed.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Typing Here")
website_label.grid(row=1, column=0)



#title timer
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=1)

timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))



# password_label = Label(text="Password")
# password_label.grid(row=3, column=0)

#Enteries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "jessemaun@gmail.com")
#
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)

#Buttons
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)

# search_button = Button(text="Search", width=13, command=find_password)
# search_button.grid(row=1, column=2)
#start button
start_button = Button( text = 'Start',  highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#reset button
reset_button = Button( text = 'Reset',  highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()


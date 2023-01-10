from tkinter import *
import math
# --------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="WORK")
    label_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    #if it's the 1st/3rd/5th/7th rep:
    #if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="BREAK", fg=RED)
    #if it's 2nd/4th/6th rep:
    elif reps % 8 == 2:
        count_down(short_break_sec)
        label_timer.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="WORK", fg=GREEN)


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
            mark += "\n✔️"
        label_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamadoro")
window.config(padx=100, pady=50, bg=YELLOW)
label_timer = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=image)
timer_text = canvas.create_text(150, 150, text="00:00", font=(FONT_NAME, 30, "bold"), fill="White")
canvas.grid(row=1, column=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

label_mark = Label(text="", fg=GREEN, bg=YELLOW)
label_mark.grid(row=4, column=1)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=2)

window.mainloop()

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = 0
timer = None

#----------------------------Null Func -----------------------------------#
def do_nothing():
	None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	window.after_cancel(timer)
	Timer.config(text = "Timer")
	Yes.config(text = "")
	canvas.itemconfig(time_text , text = "00:00")
	start.config(command = start_timer,)
	global reps
	reps = 0
	



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	start.config(command = do_nothing,)
	global reps
	reps += 1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	
	if reps % 8 == 0:
		count_down(long_break_sec)
		Timer.config(text= "Break", fg=RED)
		reps = 0
	elif reps % 2 == 0:
		count_down(short_break_sec)
		Timer.config(text= "Break", fg=PINK)
	else:
		count_down(work_sec)
		Timer.config(text= "Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

	count_minute = math.floor(count / 60)
	count_sec = count % 60 

	if count_sec == 0:
		count_sec = "00"



	canvas.itemconfig(time_text, text = f"{count_minute}:{count_sec}")
	if count > 0:
		global timer
		timer = window.after(1000, count_down , count - 1)
	else:
		start_timer()
		marks = ""
		work_sessions = math.floor(reps/2)
		for _ in range(work_sessions):
			marks += "✔"
		Yes.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100 , pady = 50, bg = YELLOW)


Timer = Label(text = "Timer", fg=GREEN , bg = YELLOW , font = (FONT_NAME, 50 , "bold"))
Timer.grid(column = 1, row = 0)


canvas = Canvas(width = 200,height = 224, bg = YELLOW, highlightthickness=0 )
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato)

time_text = canvas.create_text(103, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1 , row = 1)
Yes = Label(fg = GREEN, text = "",bg = YELLOW)
Yes.grid(column = 1 , row = 3)

start = Button(text = "Start" , highlightthickness=0, command = start_timer)
start.grid(column = 0, row = 2)



		



reset = Button(text = "RESET" , highlightthickness=0, command = reset_timer)
reset.grid(column = 2, row = 2)




window.mainloop()
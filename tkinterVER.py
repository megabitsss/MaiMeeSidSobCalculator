# for i, day in enumerate(days): #enumerate returns list of tuple ex. [("Monday", 0), ("Tuesday", 1)] etc.
#     label = Label(window, text=day, font=("Arial", 12), padx=10, pady=10)
#     label.grid(row=i+1, column=0)
#
#     spinbox = Spinbox(window, from_=0, to=16, font=("Consolas", 18))
#     spinbox.grid(row=i+1, column=1, pady=10)
from tkinter import *
from tkinter import ttk

translator = {
    "English_Speaking": "อังกฤษเพื่อการสื่อสาร",
    "Math_Admission": "คณิตศาสตร์เพื่อการศึกษาต่อ",
    "Social": "สังคมศึกษา",
    "Farming": "เกษตร",
    "Physics": "ฟิสิกส์",
    "Guidance": "แนะแนว",
    "Astronomy": "ดาราศาสตร์",
    "Math_Core": "คณิตศาสตร์พื้นฐาน",
    "PE": "พลศึกษา",
    "Chemistry": "เคมี",
    "Thai": "ภาษาไทย",
    "Math_Additional": "คณิตศาสตร์เพิ่มเติม",
    "Biology": "ชีววิทยา",
    "Physics_Admission": "ฟิสิกส์เพื่อนการศึกษาต่อ",
    "English_Core": "อังกฤษพื้นฐาน",
    "Music": "ดนตรี",
    "Club": "ชุมนุม",
}

subject_credits = {
    "English_Speaking": 8,
    "Math_Admission": 8,
    "Social": 12,
    "Farming": 8,
    "Physics": 16,
    "Guidance": 4,
    "Astronomy": 8,
    "Math_Core": 8,
    "PE": 4,
    "Chemistry": 12,
    "Thai": 8,
    "Math_Additional": 12,
    "Biology": 12,
    "Physics_Admission": 8,
    "English_Core": 8,
    "Music": 4,
    "Club": 4,
}

schedule = {
    "Monday": {"English_Speaking": 1, "Math_Admission": 1, "Social": 1, "Farming": 2, "Physics": 2, "Math_Additional": 1},
    "Tuesday": {"English_Speaking": 1, "Guidance": 1, "Astronomy": 2, "Math_Core": 1, "PE": 1},
    "Wednesday": {"Chemistry": 1, "Thai": 1, "Social": 1, "Math_Additional": 1, "Biology": 2},
    "Thursday": {"Physics_Admission": 2, "English_Core": 1, "Music": 1, "Math_Additional": 1, "Club": 1, "Biology": 1, "Thai": 1},
    "Friday": {"English_Core": 1, "Physics": 2, "Math_Core": 1, "Social": 1, "Math_Admission": 1, "Chemistry": 2}
}

subject_to_remove = []
def cal():
    global failed_subject
    failed_subject = ""
    for day, subjects in schedule.items():

        for subject in subjects:
            subject_credits[subject] -= schedule[day][subject] * int(spinboxes[day].get())

    for subject, credit in subject_credits.items():
        if credit < 0:
            subject_to_remove.append(subject)
            failed_subject += f"{translator[subject]}\n"
    if failed_subject != "":
        result.config(text=failed_subject)

    sort_credit = dict(sorted(subject_credits.items(), key=lambda item: item[1]))

    temp = ""
    for subject, existed_lesson in sort_credit.items():
        if existed_lesson >= 0:
            temp += f"{translator[subject]} เหลือ {existed_lesson} คาบ!\n"
    remaining.config(text=temp)
def clearing():
    global subject_credits
    result.config(text="Waiting for calculating..")
    remaining.config(text="Waiting for calculating..")
    subject_credits = {
        "English_Speaking": 8,
        "Math_Admission": 8,
        "Social": 12,
        "Farming": 8,
        "Physics": 16,
        "Guidance": 4,
        "Astronomy": 8,
        "Math_Core": 8,
        "PE": 4,
        "Chemistry": 12,
        "Thai": 8,
        "Math_Additional": 12,
        "Biology": 12,
        "Physics_Admission": 8,
        "English_Core": 8,
        "Music": 4,
        "Club": 4,
    }
    for day, spinbox in spinboxes.items():
        spinbox.delete(0, "end")  # Clear the current value
        spinbox.insert(0, "0")  # Set the value to zero
def update_scrollregion(event):
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

WIDTH = 400
HEIGHT = 600

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

screen_x = int((screen_width-WIDTH)/2) #need to be integer only
screen_y = int((screen_height-HEIGHT)/2)

window.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}") #+{topleftX}+{topleftY}
window.title("Mai Mee Sid Sob - Calculator")

main_frame = Frame(window)
main_frame.grid(row=0, column=0, sticky="NSEW") #1 equals True

my_canvas = Canvas(main_frame)
my_canvas.grid(row=0, column=0, sticky="NSEW")

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.grid(row=0, column=1, sticky="NS") #fill it vertically

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>", update_scrollregion)

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")



name = Label(second_frame, text="Mai Mee Sit Sob - Calculator 📱\nคุณลาหยุดไปแล้วกี่วันกันนะ ?", font=("Arial", 18))
name.grid(row=0, column=0, columnspan=2, pady=15)

spinboxes = {} #(day, spinbox(as a widget))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i, day in enumerate(days ,start=1):
    label = Label(second_frame, text=day, font=("Arial", 12), padx=10, pady=10, width=5)
    label.grid(row=i, column=0)

    spinbox = Spinbox(second_frame, from_=0, to=16, font=("Consolas", 18), width=10)
    spinbox.grid(row=i, column=1, pady=10)
    spinboxes[day] = spinbox #** Now we have a list of spinboxes (as a widget)
    #tuesday_value = spinboxes[day].get()


calculate = Button(second_frame, text="Calculate", font=("Consolas", 12), command=cal, width=15)
calculate.grid(row=6, column=0, pady=20, padx=30)

clear = Button(second_frame, text="Clear", font=("Arial", 12), command=clearing, width=15)
clear.grid(row=6, column=1, pady=20)

result_label = Label(second_frame, text="ติดมส.แล้วจ้า 👋", font=("Arial", 12))
result_label.grid(row=7,column=0, columnspan=2)
result = Label(second_frame, text="Waiting for calculating..", font=("Arial", 12))
result.grid(row=8,column=0, pady=10, columnspan=2)

remaining_label = Label(second_frame, text="---------------\nเหลือวิชาอะไรกันบ้างนะ!", font=("Arial", 12))
remaining_label.grid(row=10, column=0, columnspan=2)
remaining = Label(second_frame, text="Waiting for calculating..", font=("Arial", 12))
remaining.grid(row=11, column=0, pady=10, columnspan=2)



window.mainloop()



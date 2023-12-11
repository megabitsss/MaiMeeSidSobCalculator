#MAI MEE SID SOB Calculator
# #DEFINING -  every 0.5 credit for 4 lessons
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
        "Monday":{"English_Speaking":1, "Math_Admission":1, "Social":1, "Farming":2, "Physics":2, "Math_Additional":1},
        "Tuesday":{"English_Speaking":1, "Guidance":1, "Astronomy":2, "Math_Core":1, "PE":1},
        "Wednesday":{"Chemistry":1, "Thai":1, "Social":1, "Math_Additional":1, "Biology":2},
        "Thursday":{"Physics_Admission":2, "English_Core":1, "Music":1, "Math_Additional":1, "Club":1, "Biology":1, "Thai":1},
        "Friday":{"English_Core":1, "Physics":2, "Math_Core":1, "Social":1, "Math_Admission":1, "Chemistry":2}
}

#just a temporary list
subject_to_remove = []

for day, subjects in schedule.items():
    n = int(input(f"How many classes have you attend on {day}?: "))

    for subject in subjects:
        subject_credits[subject] -= schedule[day][subject] * n

print("----------")

for subject, credit in subject_credits.items():
    if credit < 0:
        print(f"{subject} = MAI MEE SID SOB")
        subject_to_remove.append(subject)

print("----------")

#removing subject in subject_credit (dictionary)
for subject in subject_to_remove:
    subject_credits.pop(subject)

sort_credit = dict(sorted(subject_credits.items(), key=lambda item:item[1])) #subject_credits.items() is a list with multiple tuples
#means that they get the item in subject_credits.items() for instance [ (x1,y1), (x2,y2) ] and liteally sort it by item[1] which is value

for subject, credit in sort_credit.items():
    print(f"{subject} remains {credit} lessons.")
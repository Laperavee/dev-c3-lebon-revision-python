import random
class1 = []
eleves = {"John Doe","Mac Miller","Jack Sparrow","Pablo Escobar","Chris Brown","Thomas Muller","Max Verstappen","Alex Brown"}
for names in eleves:
    eleveObj = {}
    notes = []
    for i in range (0,5):
        notes.append(random.randint(20,20))
    eleveObj["name"] = names.split(" ")[1]
    eleveObj["surname"] = names.split(" ")[0]
    eleveObj["notes"] = notes
    class1.append(eleveObj)

best_student = {}
max_note = 0
for eleve in class1:
    if max(eleve["notes"]) > max_note:
        best_student = eleve["name"], eleve["surname"]
        max_note = max(eleve["notes"])
    elif max(eleve["notes"]) == max_note:
        if eleve["name"] < best_student[0]:
            best_student = eleve["name"], eleve["surname"]
        if eleve["name"] == best_student[0]:
            if eleve["surname"] < best_student[1]:
                best_student = eleve["name"], eleve["surname"]
print(best_student)
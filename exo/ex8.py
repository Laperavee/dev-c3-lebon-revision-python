import random
class1 = []
eleves = {"John Doe","Mac Miller","Jack Sparrow","Pablo Escobar","Chris Brown","Thomas Muller","Max Verstappen","Alex Hitchens"}
for eleve in eleves:
    eleveObj = {}
    notes = []
    for i in range (0,5):
        notes.append(random.randint(0,20))
    eleveObj["nom"] = eleve.split(" ")[1]
    eleveObj["prenom"] = eleve.split(" ")[0]
    eleveObj["notes"] = notes
    class1.append(eleveObj)
from appJar import gui
import model
import controler

app = gui()
app.addLabel("en-tête", "Bienvenue à l'animalerie!")
app.setLabelBg("en-tête", "salmon")
app.setLabelFg("en-tête", "white")
app.addLabel("en-dessous", "Tableaux de bord")
app.setLabelBg("en-dessous", "gray")


liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
liste_actions = ['nourrir', 'divertir', 'coucher', 'reveiller']

for animal in liste_animaux:
    etat = model.lit_etat(animal)
    lieu = model.lit_lieu(animal)
    app.addLabel(animal, animal + ' : ' + lieu + ', ' + etat)

app.addLabel("plus bas", "Animals")
app.setLabelBg("plus bas", "gray")

for a in liste_animaux:
    app.addRadioButton("animal", a)

app.addLabel("encore plus bas", "Actions")
app.setLabelBg("encore plus bas", "gray")

for c in liste_actions:
    app.addRadioButton("action", c)

def press(act):

    action = app.getRadioButton("action")
    animal = app.getRadioButton("animal")

    if action == "nourrir":
        controler.nourrir(animal)
    if action == "divertir":
        controler.divertir(animal)
    if action == "coucher":
        controler.coucher(animal)
    if action == "reveiller":
        controler.reveiller(animal)


    for animal in liste_animaux:
        etat = model.lit_etat(animal)
        lieu = model.lit_lieu(animal)
        app.setLabel(animal, animal + ' : ' + lieu + ', ' + etat)



app.addButton("go", press)

app.go()

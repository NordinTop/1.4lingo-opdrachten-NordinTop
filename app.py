from tkinter import *
from lingo import Lingo


#lingo object
game = Lingo()

#lijst met invoervelden
invoervelden = {}

#valideer de invoer
def validate(event):
    print("beurt: " + str(game.beurt))
    print("woord: " + game.woord)
    
    invoer = invoervelden[game.beurt-1].get()
    print("ingevoerd: " + invoer)

    uitvoer = game.validate_input(invoer)
    print("resultaat: " + uitvoer)

    #toon de uitvoer
    invoervelden[game.beurt-2].insert(END, " > " + uitvoer)

    # update de status
    status_label.config(text = uitvoer)

    # update beurten
    beurten_label.config(text = str(game.beurt) + "/5")





# Main
app = Tk()
app.title("Lingo!")
app.geometry("300x400")
app.resizable(False, False)

#title
title_label = Label(app, text = "Welkom bij Lingo!", font=("Arial", 18, "bold"))
title_label.pack()

#uitleg
intro_label = Label(app, text = "Raad het woord van vijf letters in vijf beurten")
intro_label.pack()


#status
status_label = Label(app, text = "Succes!", font=("Arial", 14, "bold"), fg = 'red')
status_label.pack()


#aantal beurten
beurten_label = Label(app, text = "1/5", font=("Arial", 20, "bold"))
beurten_label.pack()


#invoervelden
for r in range(5):
    invoerveld = Entry(app, bg='#3366cc', justify=LEFT, font=('arial', 24, 'bold'), fg = 'white')
    invoerveld.pack()
    invoervelden[r] = invoerveld
    invoerveld.bind('<Return>', validate)



#Run
app.mainloop()
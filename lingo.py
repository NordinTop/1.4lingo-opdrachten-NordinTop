import sqlite3

class Lingo:
    def __init__(self):
        self.woord = self.selecteer_woord()
        self.beurt = 1

    def validate_input(self, invoer):
        self.beurt += 1

        invoer = str.lower(invoer)
        
        if (invoer == self.woord):
            return "Gewonnen"
        
        if (len(invoer) != 5):
            return "Voer een woord in van 5 letters!"

        uitvoer = ""
        for i in range(5):
            if (invoer[i] == self.woord[i]):
                uitvoer += str.upper(invoer[i])
            elif(invoer[i] in self.woord):
                uitvoer += invoer[i]
            else:
                uitvoer += "_"
        
        return uitvoer

    # Selecteer een random woord
    def selecteer_woord(self):

        # Verbinding maken met de database
        connection = sqlite3.connect("lingo.sqlite3")

        # Selecteer een woord uit de database
        cursor = connection.execute("SELECT * FROM vijfletters ORDER BY RANDOM() LIMIT 1;")
        for row in cursor:
            woord = row[0]
        connection.close()

        # Return het woord
        return woord
    
        
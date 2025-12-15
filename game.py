# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        soufrière = Room("La Soufrière", "aux pieds d'un volcan actif entouré de forêt tropicale, parfait pour une zone de montagne avec brouillard.")
        self.rooms.append(soufrière)
        chutes = Room("Les Chutes du Carbet", "près de grandes cascades au cœur de la jungle.")
        self.rooms.append(chutes)
        parc = Room("Le parc des roches gravées", "site avec des roches gravées amérindiennes remplies d'énigmes.")
        self.rooms.append(parc)
        malendure = Room("La plage de malendure", "dans une zone côtière avec fond marin protégé et pleine de surprises.")
        self.rooms.append(malendure)
        pointe = Room("La Pointe des chatêau", "dans une pointe rocheuse battue par les vagues, avec une grande croix et une vue sur l’océan.")
        self.rooms.append(pointe)
        caravelle = Room("Caravelle", "dans une grande plage paradisiaque de carte postale avec cocotiers.")
        self.rooms.append(caravelle)
        place = Room("La place de la victoire", "dans une grande place centrale avec des maisons colorées et marchés.")
        self.rooms.append(place)
        fort = Room("Le fort Napoléon", "dans une forteresse sombre qui porte les marques du passé.")
        self.rooms.append(fort)

        # Create exits for rooms

        soufrière.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": parc}
        chutes.exits = {"N" : None, "E" : place, "S" : parc, "O" : None, "U": None, "D": malendure}
        parc.exits = {"N" : chutes, "E" : None, "S" : fort, "O" : None, "U": soufrière, "D": None}
        malendure.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U": parc, "D": None}
        pointe.exits = {"N" : None, "E" : None, "S" : None, "O" : caravelle, "U": None, "D": None}
        caravelle.exits = {"N" : None, "E" : pointe, "S" : None, "O" : place, "U": None, "D": None}
        place.exits = {"N" : None, "E" : caravelle, "S" : None, "O" : chutes, "U": None, "D": None}
        fort.exits = {"N" : parc, "E" : None, "S" : None, "O" : None, "U": None, "D": None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = place

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        #Ignorer la commande vide
        if command_string.strip()=="":
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()

    def __init__(self):
        # Création des rooms, items, player, etc.
        self.room1 = Room("Malendure", "dans une zone côtière avec fond marin protégé et pleine de surprises.")
        self.room2 = Room("Soufrière", "aux pieds d'un volcan actif entouré de forêt tropicale, parfait pour une zone de montagne avec brouillard.")
        # Exemple d’items dans la map :
        self.room1.inventory["Buste"] = Item("Buste", "un buste du commandant Cousteau", 2)
        self.room2.inventory["Epée"] = Item("Epée", "une épée avec une lame forgée à base de roche volcanique", 1)

        self.player = Player(self.room1, max_weight=5)

        self.actions = Actions(self)
        self.command_processor = CommandProcessor(self.actions)

    def loop(self):
        while True:
            line = input("> ")
            if line.strip() in ("quit", "exit"):
                break
            self.command_processor.execute(line)

if __name__ == "__main__":
    game = Game()
    game.loop()

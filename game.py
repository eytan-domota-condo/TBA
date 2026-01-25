# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from character import Character
from quest import Quest

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):
        """Initialize the game with rooms, commands, and quests."""
        self._setup_commands()
        self._setup_rooms()
        self._setup_player()
        self._setup_quests()


    # Setup commands
    def _setup_commands(self):
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : retour à la salle précédente", Actions.back,0)
        self.commands["back"]=back
        look = Command("look", " : regarder autour de soi", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <objet> : prendre un objet", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <objet> : déposer un objet", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : vérifier l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        self.commands["quests"] = Command("quests"
                                          , " : afficher la liste des quêtes"
                                          , Actions.quests
                                          , 0)
        self.commands["quest"] = Command("quest"
                                         , " <titre> : afficher les détails d'une quête"
                                         , Actions.quest
                                         , 1)
        self.commands["activate"] = Command("activate"
                                            , " <titre> : activer une quête"
                                            , Actions.activate
                                            , 1)
        self.commands["rewards"] = Command("rewards"
                                           , " : afficher vos récompenses"
                                           , Actions.rewards
                                           , 0)
        
    # Setup rooms
    def _setup_rooms(self):
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

       
        from item import Item

        sword = Item("sword", "une épée égarée", 2)
        rocheloge = Item("rocheloge", "une petite pierre qui informe du temps qui passe", 0.1)
        buste = Item("buste","un buste du Commandant Cousteau",5)
        croix = Item("croix","une croix face à la mer",10)
        bouteillevide = Item("bouteillevide","Tous les chemins mènent au rhum !",0.5)
        pierrefeu = Item("pierrefeu","Brulante comme les flammes, elle brille comme une étoile",1)

        fort.add_item(sword)
        parc.add_item(rocheloge)
        malendure.add_item(buste)
        pointe.add_item(croix)
        caravelle.add_item(bouteillevide)
        soufrière.add_item(pierrefeu)
        
        ary  = Character("Ary", "un guide pas comme les autres", place, ["Je suis Ary, ton guide pour cette nouvelle aventure.", "Regarde les quêtes que tu dois réaliser","Reviens me parler une fois toutes les quêtes terminées. Petit conseil : A la pointe tu dois aller et une épreuve de force tu vas réaliser !"])
        place.characters[ary.name.lower()] = ary  # nom en minuscules pour la commande

        fantome = Character("Fantome", "un fantome très énigmatique", fort, ["N'ayez crainte ! Je suis le propriétaire", "Trouvez mon épée égarée et recevez votre récompense"])
        fort.characters[fantome.name.lower()] = fantome

        général  = Character("Général", "le général a une mission pour vous !", malendure, ["Je suis le général Cousteau !", "Ramène moi mon buste soldat mais prend garde aux poissons !"])
        malendure.characters[général.name.lower()] = général 

        volcanologue  = Character("Volcanologue", "un expert au sommet du volcan", soufrière, ["Je suis le Volcanologue de cette vielle dame !", "Je cherche une pierre pas comme les autres. Aide moi à la retrouver je t'en prie !!"])
        soufrière.characters[volcanologue.name.lower()] = volcanologue

        archéologue  = Character("Archéologue", "un explorateur des vestiges du passé", parc, ["Je suis l'archéologue responsable de cette fouille !", "Ramenez moi la roche qui indique le temps passé, présent, futur !"])
        parc.characters[archéologue.name.lower()] = archéologue

        bobby = Character("Bobby", "un amoureux de la boisson", caravelle, ["Je suis le barman de cette plage. Bois ! Tu m'en diras des nouvelles", "Finissons cette bouteille mon ami !","Tu ne partiras pas de cette plage si la bouteille est pleine !"])
        caravelle.characters[bobby.name.lower()] = bobby

        talk = Command("talk", " <pnj> : parler à un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk

    def _setup_player(self, player_name=None):
        """Initialize the player."""
        if player_name is None:
            player_name = input("\nEntrez votre nom: ")

        self.player = Player(player_name)
        self.player.current_room = self.rooms[6]  


    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Grand Explorateur",
            description="Explorez tous les lieux de ce monde mystérieux.",
            objectives=["Visiter malendure"
                        , "Visiter fort"
                        , "Visiter chutes"
                        , "Visiter caravelle"
                        , "Visiter pointe"],
            reward="Titre de Grand Explorateur"
        )

        travel_quest = Quest(
            title="Grand Voyageur",
            description="Déplacez-vous 10 fois entre les lieux.",
            objectives=["Se déplacer 10 fois"],
            reward="Bottes de voyageur"
        )

        discovery_quest = Quest(
            title="Découvreur de Secrets",
            description="Découvrez les trois lieux les plus mystérieux.",
            objectives=["Visiter soufrière"
                        , "Visiter fort"
                        , "Visiter place"],
            reward="Clé dorée"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(travel_quest)
        self.player.quest_manager.add_quest(discovery_quest)
    
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

        #Ignorer commande vide
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

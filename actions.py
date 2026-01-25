# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.

# The error message is stored in the MSG0 and MSG1 variables and formatted
# with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from item import Item
class Actions:

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a direction (N, E, S, O, U, D).
        """
        player = game.player
        l = len(list_of_words)

        # Vérif du nombre de paramètres
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupérer la direction brute
        raw_dir = list_of_words[1].strip().upper()

        # Table de correspondance texte -> direction canonique
        direction_map = {
            "N": "N", "NORD": "N",
            "E": "E", "EST": "E",
            "S": "S", "SUD": "S",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U",
            "D": "D", "DOWN": "D"
        }

        # Vérifier que la direction existe dans le mapping
        if raw_dir not in direction_map:
            print("\nDirection invalide. Utilisez N, E, S, O, U ou D.\n")
            return False

        # Direction normalisée (N/E/S/O/U/D)
        direction = direction_map[raw_dir]

        # Vérifier que la direction normalisée est autorisée pour le joueur
        if direction not in player.valid_directions:
            print("\nDirection invalide. Utilisez N, E, S, O, U ou D.\n")
            return False

        # Déplacement
        player.move(direction)
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.help(game, ["help"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Voici les commandes disponibles:
            - help : afficher cette aide
            - quit : quitter le jeu
            - go <direction> : se déplacer dans une direction cardinale (N, E, S, O)
            - quests : afficher la liste des quêtes
            - quest <titre> : afficher les détails d'une quête
            - activate <titre> : activer une quête
            - rewards : afficher vos récompenses
        <BLANKLINE>
        True
        >>> Actions.help(game, ["help", "N"], 0)
        <BLANKLINE>
        La commande 'help' ne prend pas de paramètre.
        <BLANKLINE>
        False
        >>> Actions.help(game, ["help", "N", "E"], 0)
        <BLANKLINE>
        La commande 'help' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

        """
        Print the list of available commands.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
# dans game.py ou actions.py

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        if len(player.history) == 0:
            print("Vous ne pouvez pas encore revenir en arrière.\n")
            return False
        previous_room = player.history.pop()
        player.current_room = previous_room
        print(player.current_room.get_long_description())
        print(player.get_history())
        return True



    @staticmethod
    def look(game, words, number_of_parameters):
        room = game.player.current_room
        print(room.get_long_description())
        print(room.get_items_description())
        print(room.get_characters_description())

    @staticmethod
    def take(game, words, number_of_parameters):
        if len(words) < 2:
            print("Prendre quoi ?")
            return

        item_name = words[1].lower()

        print(game.player.take(item_name))

        # informer les quêtes
        game.player.quest_manager.check_action_objectives(
            "prendre",
            item_name
        )
        game.player.quest_manager.check_activate_final_quest()


    @staticmethod
    def drop(game, words, number_of_parameters):
        if len(words) < 2:
            print("Déposer quoi ?")
            return
        print(game.player.drop(words[1]))

    @staticmethod
    def check(game, words, number_of_parameters):
        print(game.player.get_inventory_description())

    @staticmethod
    def talk(game, words, number_of_parameters):
        if len(words) < 2:
            print("Parler à qui ?")
            return
        pnj_name = words[1].lower()
        room = game.player.current_room
        if pnj_name not in room.characters:
            print(f"Il n'y a pas de personnage '{words[1]}' ici.")
            return
        pnj = room.characters[pnj_name]
        print(pnj.get_msg())

        if game.player.quest_manager:
            game.player.quest_manager.check_action_objectives("parler avec", pnj_name)
            game.player.quest_manager.check_activate_final_quest()

    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        return True


    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True


    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True

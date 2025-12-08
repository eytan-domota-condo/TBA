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


class Actions:

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

    def help(game, list_of_words, number_of_parameters):
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

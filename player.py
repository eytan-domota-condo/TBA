# Define the Player class.
class Player():

    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.valid_directions = ("N", "E", "S", "O", "U", "D")
        # Historique des pièces visitées (pile)
        self.history = []

    def move(self, direction):
        direction = direction.upper()
        next_room = self.current_room.exits.get(direction, None)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Empiler la salle actuelle dans l'historique avant de bouger
        self.history.append(self.current_room)

        self.current_room = next_room
        print(self.current_room.get_long_description())
        # Historique après chaque déplacement
        print(self.get_history())
        return True

    def get_history(self):
        """
        Retourne une chaîne représentant l'historique des pièces visitées.
        """
        if len(self.history) == 0:
            return "\nVous n'avez encore visité aucun autre lieu.\n"

        lines = ["\nVous avez déja visité les pièces suivantes:"]
        for room in self.history:
            lines.append("    - " + room.description)
        return "\n".join(lines) + "\n"
    

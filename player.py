# Define the Player class.
class Player():

    def __init__(self, name, max_weight=5.0):
        self.name = name
        self.current_room = None
        self.valid_directions = ("N", "E", "S", "O", "U", "D")
        # Historique des pièces visitées (pile)
        self.history = []
        self.inventory = {}
        self.max_weight = max_weight

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


    def take(self, item_name):
        item = self.current_room.remove_item(item_name)
        if item is None:
            return f"L'objet '{item_name}' n'est pas ici."

        # Vérification du poids
        if self.current_weight() + item.weight > self.max_weight:
            # Remettre l’objet dans la salle
            self.current_room.add_item(item)
            return f"Vous ne pouvez pas prendre '{item_name}' : trop lourd !"

        # Sinon, prendre l’objet
        self.inventory[item_name] = item
        return f"Vous avez pris l'objet '{item_name}'."

    def drop(self, item_name):
        item = self.inventory.pop(item_name, None)
        if item is None:
            return f"Vous n'avez pas l'objet '{item_name}'."
        self.current_room.add_item(item)
        return f"Vous avez déposé l'objet '{item_name}'."

    def get_inventory_description(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        result = f"Votre inventaire contient ({self.current_weight():.1f}/{self.max_weight} kg) :\n"
        for item in self.inventory.values():
            result += f"  - {item}\n"
        return result


    def current_weight(self):
        """Retourne le poids total des objets dans l’inventaire."""
        total = 0
        for item in self.inventory.values():
            total += item.weight
        return total

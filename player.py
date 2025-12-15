# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        # Toutes les directions valides (cardinales + verticales)
        self.valid_directions = ("N", "E", "S", "O", "U", "D")
        
    # Define the move method.
    def move(self, direction):
        # On sécurise en majuscules
        direction = direction.upper()

        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction, None)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def __init__(self, starting_room, max_weight: int | float = 5):
        self.current_room = starting_room
        self.history = []
        self.inventory: dict[str, Item] = {}
        self.max_weight = max_weight

    def get_inventory_weight(self) -> float:
        return sum(item.weight for item in self.inventory.values())

    def get_inventory(self) -> str:
        if not self.inventory:
            return "Votre inventaire est vide."
        lines = ["Vous disposez des items suivants :"]
        for item in self.inventory.values():
            lines.append(f"- {item}")
        return "\n".join(lines)

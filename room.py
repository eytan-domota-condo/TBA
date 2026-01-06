# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = {}
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item_name):
        return self.items.pop(item_name, None)

    def get_items_description(self):
        if not self.items:
            return "Il n'y a aucun objet ici."
        result = "Objets visibles :\n"
        for item in self.items.values():
            result += f"  - {item}\n"
        return result

    # méthode pour afficher les PNJ présents
    def get_characters_description(self):
        if not self.characters:
            return ""
        result = "Personnages présents :\n"
        for char in self.characters.values():
            result += f"  - {char}\n"
        return result

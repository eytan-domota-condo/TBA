class Character:
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room  # salle où se trouve le PNJ
        self.msgs = msgs[:]  # copie de la liste de messages
        self._index = 0      # pour donner les messages cycliquement

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self.msgs:
            return f"{self.name} ne dit rien."
        msg = self.msgs[self._index]
        self._index = (self._index + 1) % len(self.msgs)  # cyclique
        return f"{self.name} dit : {msg}"

    def move(self):
        """Optionnel : déplacement automatique du PNJ"""
        from random import choice, random
        exits = [room for room in self.current_room.exits.values() if room is not None]
        if exits and random() < 0.5:
            self.current_room = choice(exits)
            return True
        return False

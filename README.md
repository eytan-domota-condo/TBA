# TBA

Ce repo contient la version de mon jeu d'aventure qui a pour objectif de faire découvrir les lieux emblématique de la Guadeloupe.

Les lieux sont au nombre de 8 et dans chacuns de ses lieux se trouve des secrets a dénicher. Il y a 6 PNJs différents et chacuns peut vous aider progresser en vous remmettant un objet indispensable pour votre réussite. 

Car en effet pour gagner il vous faut réussir l'intégralité des quêtes qui sont au nombre de 5.

## Structuration

Il y a pour le moment 8 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre ;
- `character.py` / `Character` : les personnages du jeu.
- `quest.py` / `Quest` : les quêtes du jeu ;
- `item.py` / `Item` : les objets que l'on peut retrouver dans le jeu .
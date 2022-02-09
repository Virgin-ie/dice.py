"""
Configurer le diagramme ASCII des faces de dés

Dessinez six faces de dés en utilisant les caractères ASCII.
Chaque face de dés dans ce diagramme reflète la valeur qui résulte d'une itération de la simulation.
"""
# stocker les faces dans 'DICE_ART', un dictionnaire qui associe chaque face à sa valeur entière correspondante
DICE_ART = {
    1: (
        "___________",
        "|         |",
        "|         |",
        "|    °    |",
        "|         |",
        "|_________|"
    ),
    2: (
        "___________",
        "|         |",
        "|  °      |",
        "|         |",
        "|      °  |",
        "|_________|"
    ),
    3: (
        "___________",
        "|         |",
        "|  °      |",
        "|    °    |",
        "|      °  |",
        "|_________|"
    ),
    4: (
        "___________",
        "|         |",
        "|  °   °  |",
        "|         |",
        "|  °   °  |",
        "|_________|"
    ),
    5: (
        "___________",
        "|         |",
        "|  °   °  |",
        "|    °    |",
        "|  °   °  |",
        "|_________|"
    ),
    6: (
        "___________",
        "|         |",
        "|  °   °  |",
        "|  °   °  |",
        "|  °   °  |",
        "|_________|"
    ),
}
# contient le nombre de rangées qu'une face donné ocupera (cinq rangés)
DIE_HEIGHT = len(DICE_ART[1])
# défini 'DIE_WIDTH' pour contenir le nombre de colonnes nécessaires pour dessiner une face de dés (11 caractères)
DIE_WIDTH = len(DICE_ART[1][0])
# définit 'DIE_FACE_SEPARATOR' qui contient un caractère d'espacement
DIE_FACE_SEPARATOR = " "

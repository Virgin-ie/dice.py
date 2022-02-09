# Lancer le programme dans le shell powershell
# Projet suivi sur Real Python,
# crédit Leodanis Pozo Ramos, jan 19 2022 'Build a Dice-Rolling Application With Python'
import random
import dice_art


# Définit la chaîne d'entrée comme argument
def parse_input(input_string):
    """
    Renvoie 'input_string' sous la forme d'un entier compris entre 1 et 6

    Vérifie si 'input_string' est un nombre entier compris entre 1 et 6.
    Si oui -> retourne un entier avec la même valeur.
    Sinon, dire à l'utilisateur d'entrer un numéro valide et de quitter le programme.
    """
    # Vérifie si l'entrée utilisateur est une valeur valide
    # l'appel à '.strip()' supprime tous les espaces indésirables autour de la chaîne d'entrée
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)   # convertit l'entrée en un nombre entier et la renvoie à l'appelant
    else:
        print("Merci d'entrer un nombre entre 1 et 6")
        # quitte l'application avec une exception 'SystemExit' et un code d'état '1'
        # pour signaler que quelque chose c'est mal passé
        raise SystemExit(1)


# définit 'roll_dice' qui prend un argument représentant le nombre de dés à lancer dans un appel donné
def roll_dice(num_dice):
    """
    Renvoie une liste d'entiers de longueur 'num_dice'

    Chaque entier de la liste retournée est un nombre aléatoire entre 1 et 6 inclus.
    """
    # créer une liste vide pour stocker les résultats de la simulation de lancer de dés
    roll_results = []
    # définit une boucle 'for' qui itère une fois pour chaque dés que l'utilisateur veut lancer
    for _ in range(num_dice):
        # appel 'randint()' pour générer un nombre entier pseudo-aléatoire de 1 à 6 inclus
        # Cet appel génère un numéro unique à chaque itération. Ce nombre représente le résultat du lancer d'un dés à
        # six faces
        roll = random.randint(1, 6)
        # ajoute le résultat actuel du lancer de sés dans 'roll_results'
        roll_results.append(roll)
    # renvoie la liste des résultats de la simulation de lancer dés
    return roll_results


# définit 'generate_dice_faces_diagram()' avec 1 seul argument appelé 'dice_values'.
# cet argument contiendra la liste des valeurs entières du lancer de dés résultant de l'appel à 'roll_dice()'
def generate_dice_faces_diagram(dice_values):
    """
    Renvoie un diagramme ASCII des faces de dés à partir de 'dice_values'.

    La chaîne renvoyer contient une représentation ASCII de chaque dés
    Par exemple si 'dice_values' = [4, 1, 2] alors la chaîne retourné ressemble à ceci :

    ~~~~~~~~~~~~~~~~~~RESULTS~~~~~~~~~~~~~~~~
    ___________    ___________    ___________
    |         |    |         |    |         |
    |  °   °  |    |         |    |  °      |
    |         |    |    °    |    |         |
    |  °   °  |    |         |    |      °  |
    |_________|    |_________|    |_________|
    """
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # générer un entête avec le mot "résultats" centré
    # créer une variable temporaire 'width' pour contenir le diagramme des faces de dés actuel
    width = len(dice_faces_rows[0])
    # créer un entête affichant le mot 'RESULTATS'
    # qui utilise 'str.center()' les diagrammes 'width' et le symbole tilde '~' comme arguments
    diagram_header = " RESULTATS ".center(width, "~")

    # génére une chaîne contenant le diagramme final des faces du dés
    # "\n" fonctionne comme un séparateur de ligne
    # l'argument '.join()' est une liste de chaîne concaténant l'entête du diagramme et les chaînes (lignes) qui
    # façonne les faces des dés
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    # renvoie un diagramme de faces de dés prêt à imprimer à l'appelant
    return dice_faces_diagram


def _get_dice_faces(dice_values):
    # générer une liste de faces de dés à partir de 'DICE_ART'
    # créer une liste vide 'dice_faces' pour stocker les faces de dés correspondant à la liste d'entrée des valeurs
    # de dés. C'est faces de dés s'afficheront dans le diagramme ASCII final.
    dice_faces = []
    # définit une boucle 'for' pour parcourir les valeurs des dés
    for value in dice_values:
        # récupère la face de dés correspondant à la valeur de dés actuelle de 'DICE_ART' et l'ajoute à 'dice_faces'
        dice_faces.append(dice_art.DICE_ART[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces):
    # générer une liste contenant les rangées de faces de dés
    # créer une liste vide pour contenir les lignes dans le diagramme final des faces de dés
    dice_faces_rows = []
    # définit une boucle 'for' qui itère sur les indices de '0' à 'DIE_HEIGHT'
    # chaque index représente l'index d'une ligne donnée dans le diagramme des faces de dés
    for row_idx in range(dice_art.DIE_HEIGHT):
        # définit 'row_component' comme une liste vide pour contenir des parties des faces de dés qui rempliront
        # une ligne donnée
        row_components = []
        # boucle 'for' pour iérer sur les faces des dés
        for die in dice_faces:
            # stocke chaque composant de ligne
            row_components.append(die[row_idx])
        # join les composants de ligne dans une chaîne de ligne finale, séparant les composants individuels par
        # des espaces
        row_string = dice_art.DIE_FACE_SEPARATOR.join(row_components)
        # ajoute chaque chaîne de ligne à la liste contenant les lignes qui façonneront le diagramme final
        dice_faces_rows.append(row_string)
    return dice_faces_rows


# Bloc de code principal de l'application

# 1 - Obtenir et valider l'entrée utilisateur
num_dice_input = input("Combien de dès voulez-vous lancer ? [1-6]")
num_dice = parse_input(num_dice_input)

# 2 - Lancer les dés
# appel 'roll_dice' avec 'num_dice' comme argument
roll_results = roll_dice(num_dice)

# 3 - générer le diagramme ASCII des faces de dés
# appel 'generate_dice_faces_diagram()' avec 'roll_results' comme argument
# cet appel construit et renvoie un diagramme de faces de dés qui correspond aux résultats actuels du lancer de dés
dice_face_diagram = generate_dice_faces_diagram(roll_results)

# 4 - afficher le schéma
print(f"\n{dice_face_diagram}")

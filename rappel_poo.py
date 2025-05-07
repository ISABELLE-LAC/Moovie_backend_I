# Qu'est-ce qu'un objet ?

# Un objet est une entité qui combine des données (qu’on appelle des attributs) et des actions (appelées méthodes).
# C’est comme une petite boîte avec :

#     Ce qu’elle contient → les attributs

#     Ce qu’elle sait faire → les méthodes

# Exemple de la vie réelle :
# Un chien est un objet. Il a des attributs (nom, race, âge) et des méthodes (aboyer, courir, manger).

######### La Classe ##########

    # Une classe est un modèle ou un plan pour fabriquer des objets.

# %%
class Chien:
    pass

########### L'objet (ou instance) ##########

    # Une instance est un objet créé à partir d'une classe.

# %%
mon_chien = Chien()
print(type(mon_chien))  # <class '__main__.Chien'>

    # Maintenant, mon_chien est un objet de la classe Chien.

 
########## Attributs ##########

    # Les attributs sont des informations propres à chaque objet.

# %%
# Redéfinissons la classe Chien pour y ajouter des attributs.
class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

# __init__ est une méthode spéciale appelée automatiquement quand on crée un objet.

# self fait référence à l’objet lui-même.

# name et breed sont des attributs.


# %%
# (Re)Créons un objet de la classe Chien avec des attributs.
mon_chien = Chien("Pipo", "Labrador")
print(mon_chien.nom)   # Pipo
print(mon_chien.race)  # Labrador


########## Méthodes ##########
    # Les méthodes sont des actions que l'objet peut effectuer.

# %%
    # Ajoutons des méthodes à notre classe Chien.   

class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

    def aboyer(self):
        print(f"{self.nom} dit : Wouf !")

# %%

rex = Chien("Rex", "Berger Allemand")
rex.aboyer()  # Rex dit : Wouf !


#  Pourquoi c’est utile ?

# Créer ses propres classes permet de :

#     Structurer son code de manière claire et réutilisable.

#     Organiser les données avec logique (comme on le fera avec nos tables SQL).

#     Encapsuler des comportements, pour éviter le code dupliqué ou mal organisé.
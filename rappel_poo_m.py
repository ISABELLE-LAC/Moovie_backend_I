###### Classes  #######

#%%
class Chien :
   pass 

#### Objet (Instance) ####


#%%
mon_chien = Chien()
type(mon_chien)

##### Attribut #####
# %%

class Chien:
   def __init__(self, nom, race):
      self.nom = nom
      self.race = race
# %%
mon_chien=Chien("Titi", "Chiwawa")
print(mon_chien.nom)
print(mon_chien.race)
      
#### Méthodes ####
#Les actions que l'objet peut effectuer
# %%
class Chien:
   def __init__(self, nom, race):
      self.nom = nom
      self.race = race
   
   def aboyer(self):
      print(f"{self.nom} aboie!")
      

# %%
mon_chien.aboyer()
# %%
mon_chien=Chien("Titi","berger allemand")
mon_chien.aboyer()
# %%

""" 
L'objectif de ce fichier est de tester les fonction d'aide de simplification des requetes SQLALchemy defini dans le fichier query_helper.py.

"""

### Import
# %%
from database import SessionLocal # objet pour définir la session
from query_helper import *

#%%

# test1: récupérer le film dont l'ID est 1
db = SessionLocal()

movie = get_movie(db, movie_id=1)
print(movie.title, movie.genres)
# %%
# Test2: la fonction get_movies

movies = get_movies(db, limit = 7)
for movie in movies:
   print(f"ID: {movie.movieId}, titre: {movie.title}, genre: {movie.genres}")

# %%
# Test 3: La fonction get_ratings

ratings = get_ratings(db, limit = 7)
for eval in ratings:
   print(f"ID utilisateur: {eval.userId}, ID film: {eval.movieId}, Score: {eval.rating}")
# %%
# Test 4: Les fonctions de requête analytique
print(f" Le nombre total de film est : {get_movie_count(db)}")
print (f"Le nombre d'évaluation est {get_rating_count(db)}")
print(f"Le nombre de tag effectué est {get_tag_count(db)}")
print(f"Le nombre de lin=gne dans la table links est {get_link_count(db)}")


#%%
# Fermer la session pour la suite
db.close() 

# %%

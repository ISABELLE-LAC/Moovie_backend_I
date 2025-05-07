""" 
L'objectif de ce fichier est de se rassurer que le modèle de données défini dans le fichier models.py a été bien défini. 
Pour ce faire, nous commençons par définir une session qui nous permet par la suite de faire des requêtes dans les différentes tables à l'aide du module query.
A la fin nous fermons bien la session afin de fermer la connection à la base.

"""

### Import
# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

### Creer (Ouvrir) une session local

db = SessionLocal()

# %%

# Tester la récupération de quelques films
movies = db.query(Movie).limit(10).all()
#print(movies) emplacement des objets

for movie in movies:
   print(f" ID : {movie.movieId}, titre : {movie.title}, genre: {movie.genres}")

else: 
   print("Aucun film trouvé")      
# %%

# Récupérer les films dont le genre est action
action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(7).all()
for movie in action_movies:
   print(f" ID : {movie.movieId}, titre : {movie.title}, genre: {movie.genres}")




# %%
### Tester la récupération des évaluations (ratings)
ratings = db.query(Rating).limit(7).all()
for eval in ratings:
   print(f"ID film:{eval.movieId}, ID user : {eval.userId}, Note: {eval.rating}, date: {eval.timestamp}")
# %%

# Récupérer les films dont la note est supérieure à 4
### Méthode 1 tenir en compte du fait que les relations entre les tables ont été bien définies.
hight_rate_movie = (
   db.query(Movie.title, Rating.rating)
   .join(Rating)
   .filter(Rating.rating >= 4)
   .limit(7)
   .all()
)

for titre, note in hight_rate_movie:
   print(titre, note)

# %%
### Deuxième méthode Utiliser nativement les méthodes de sQL cad en tenant compte des ID
hight_rate_movie = (
   db.query(Movie.title, Rating.rating)
   .join(Rating)
   .filter(Rating.rating >= 4, Movie.movieId == Rating.movieId)
   .limit(7)
   .all()
)

for titre, note in hight_rate_movie:
   print(titre, note)
# %%

### Récupérer les tags associés au film
tags = db.query(Tag).limit(7).all()
for tag in tags:
   print(f"ID movie: {tag.movieId}, tag: {tag.tag}")
# %%
### Tester la classe Link

links = db.query(Link).limit(7).all()
for link in links:
   print(f"ID film: {link.movieId}, ID dans tmdb: {link.tmdbId}, ID dans imdb : {link.imdbId}")
# %%
# fermer la connection à la base, fermer la session
db.close()

# %%

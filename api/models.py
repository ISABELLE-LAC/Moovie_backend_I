""" Définition des modèles de données avec SQLALchemy"""

""" Un modèle içi est une classe Python. On veut recréer la base de données en utilisant des objets python. Les attributs sont les colonnes de la table """

""" L'objectif ici est de définir la version python (SQLALchemy) de la structure de notre base de données,
Le but étant de manipuler les données de manière simple et intuitive. En utilisant les outils de Python
"""

### Import

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship # permet les créations de clés étrangères entre les tables
from database import Base # toutes les classes crées içi hérite de cet objet Base

### Movies

class Movie(Base):
   __tablename__ = "movies" # pour indiquer que cette classe appartient à la table movies

   # Définition des colonnes (utiliser les mêmes noms de colonnes de movies.csv)
   movieId = Column(Integer, primary_key=True, index=True)
   title = Column(String, nullable=False)
   genres = Column(String)

   # Définir les relations entre les tables en utilisant la fonction relationship
   ratings = relationship("Rating", back_populates="movie", cascade="all, delete") # chaque évaluation est lié à un film
   tags = relationship("Tag", back_populates="movie", cascade="all, delete") # chaque évaluation est lié à un film
   links = relationship("Link", back_populates="movie", uselist=False, cascade="all, delete") # il y'a un seul lien par film


class Rating(Base):
    __tablename__ = "ratings"
    # Définir les colonnes
    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    rating = Column(Float)
    timestamp = Column(Integer)
    # Définir les relations avec les autres tables
    movie = relationship("Movie", back_populates="ratings")


class Tag(Base):
    __tablename__ = "tags"
    # Définir les colonnes
    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    tag = Column(String, primary_key=True)
    timestamp = Column(Integer)
    # Définir les relations avec les autres tables
    movie = relationship("Movie", back_populates="tags")


class Link(Base):
    __tablename__ = "links"
    # Définir les colonnes
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    imdbId = Column(String) # id du film dans la base imdb, ces deux permettent d'avoir l'affiche, le poster du film
    tmdbId = Column(Integer) # id du film dans la base tmdb
    # Définir les relations avec les autres tables
    movie = relationship("Movie", back_populates="links")

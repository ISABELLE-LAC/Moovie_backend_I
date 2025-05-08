"""
Définition des shemas Pydantic pour la validation des données de l'API FastAPI.

Un shema Pydantic est une classe spéciale basé sur BaseModel et qui permet de valider automatiquement les données,
 les sérialiser et générer automatiquement la documentation.

Ce fichier défini les shémas de données utilisés dans notre API afin de:
  - Structurer ce que l'API envoie (en sortie dans les réponses)
  - Valider ce que l'API reçoit (en entrée dans les requêtes)

Ces shemas utilisent pydantic, une bibliothèque de validation des données très utilisée avec FastAPI.
"""

### Importation

from pydantic import BaseModel # Tous les shemas héritent de BaseModel
from typing import Optional, List # le champ peut être optionnel et on peut attendre d'une liste


### --- Schémas secondaires (associé au films)  --- 
# Les différentes classes définissent les données associées au films à savoir (notes, tags et liens)
# orm_mode = True, indique à FastAPI qu'on peut créer ce schéma à partir d’un objet SQLAlchemy (ce qui est le cas dans ce projet)

# Note liée à un film
class RatingBase(BaseModel): 
    userId: int 
    movieId: int 
    rating: float 
    timestamp: int 

    class Config: 
        orm_mode = True 

# tag lié à un film
class TagBase(BaseModel): 
    userId: int 
    movieId: int 
    tag: str 
    timestamp: int 

    class Config: 
        orm_mode = True 

# lien IMDB ou TMDB
class LinkBase(BaseModel): 
    imdbId: Optional[str] 
    tmdbId: Optional[int] 

    class Config: 
        orm_mode = True 



### --- Schéma principal pour Movie --
class MovieBase(BaseModel): 
    movieId: int 
    title: str 
    genres: Optional[str] = None 

    class Config: 
        orm_mode = True 

#  Détail complet pour les films
class MovieDetailed(MovieBase): 
    ratings: List[RatingBase] = [] 
    tags: List[TagBase] = [] 
    link: Optional[LinkBase] = None


 # --- Schéma pour liste de films (sans détails imbriqués) --
class MovieSimple(BaseModel): 
    movieId: int 
    title: str 
    genres: Optional[str] 

    class Config: 
        orm_mode = True 


# --- Pour les endpoints de /ratings et /tags si appelés seuls --
class RatingSimple(BaseModel): 
    userId: int 
    movieId: int 
    rating: float 
    timestamp: int 

    class Config: 
        orm_mode = True 

class TagSimple(BaseModel): 
    userId: int 
    movieId: int 
    tag: str 
    timestamp: int 

    class Config: 
        orm_mode = True 

class LinkSimple(BaseModel): 
    movieId: int 
    imdbId: Optional[str] 
    tmdbId: Optional[int] 

    class Config: 
        orm_mode = True
"""Database configuration"""

### Import
from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker 

### Chemein vers la base de données (elle est dans le même dossiers que le fichier python)
SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db" 

# # Créer un moteur de base de données (engine) qui établit la connexion avec notre base SQLite (movies.db). 
# connect_args pour accepter les traitement en parralèles (utilisation de la même connection dans plusers thread)
engine = create_engine( 
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
) 


# Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données. 
#Notre API est en lecture seul,
# valider les transaction manuellement
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy. 
Base = declarative_base() 

# pour exécuter une vérification de la connexion à la base de données (peut être utile pour le débogage ou la configuration initiale).
#ctrlk+ctrl c: commenter bloc et pour decommenter ctrl K + ctrl U
# if __name__ == "__main__":
#      try:
#          with engine.connect() as conn:
#             print("Connexion à la base de données réussie.")
#      except Exception as e:
#         print(f"Erreur de connexion : {e}")
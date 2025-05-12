import os
from dotenv import load_dotenv

load_dotenv()

class MovieConfig:
    """Classe de configuration contenant des arguments pour le client SDK.

    Contient la configuration de l'URL de base et du backoff progressif.
    """

    movie_base_url: str
    movie_backoff: bool
    movie_backoff_max_time: int

    def __init__(
        self,
        movie_base_url: str = None,
        backoff: bool = True,
        backoff_max_time: int = 30,
    ):
        """Constructeur pour la classe de configuration.

        Contient des valeurs d'initialisation pour écraser les valeurs par défaut.

        Args:
        movie_base_url (optional):
            L'URL de base à utiliser pour tous les appels d'API. Transmettez-la ou définissez-la dans une variable d'environnement.
        movie_backoff:
            Un booléen qui détermine si le SDK doit réessayer l'appel en utilisant un backoff lorsque des erreurs se produisent.
        movie_backoff_max_time:
            Le nombre maximal de secondes pendant lesquelles le SDK doit continuer à essayer un appel API avant de s'arrêter.
        """

        self.movie_base_url = movie_base_url or os.getenv("MOVIE_API_BASE_URL")
        print(f"MOVIE_API_BASE_URL in MovieConfig init: {self.movie_base_url}")  

        if not self.movie_base_url:
            raise ValueError("L'URL de base est requise. Définissez la variable d'environnement MOVIE_API_BASE_URL.")

        self.movie_backoff = backoff
        self.movie_backoff_max_time = backoff_max_time

    def __str__(self):
        """Fonction Stringify pour renvoyer le contenu de l'objet de configuration pour la journalisation"""
        return f"{self.movie_base_url} {self.movie_backoff} {self.movie_backoff_max_time}"
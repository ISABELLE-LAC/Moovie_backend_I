# MovieLens SDK - `movieIsdk`

Un SDK Python simple pour interagir avec l’API REST MovieLens. Il est conçu pour les **Data Analysts** et **Data Scientists**, avec une prise en charge native de **Pydantic**, **dictionnaires** et **DataFrames Pandas**.

[![PyPI version](https://badge.fury.io/py/movieIsdk.svg)](https://badge.fury.io/py/movieIsdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Installation

```bash
pip install movieIsdk
```

---

## Configuration

```python
from movieIsdk import MovieClient, MovieConfig

# Configuration avec l’URL de votre API (Render ou locale)
config = MovieConfig(movie_base_url="https://moovie-backend-i.onrender.com")
client = MovieClient(config=config)
```

---

## Tester le SDK

### 1. Health check

```python
client.health_check()
# Retourne : {"status": "ok"}
```

### 2. Récupérer un film

```python
movie = client.get_movie(1)
print(movie.title)
```

### 3. Liste de films au format DataFrame

```python
df = client.list_movies(limit=5, output_format="pandas")
print(df.head())
```

---

## Modes de sortie disponibles

Toutes les méthodes de liste (`list_movies`, `list_ratings`, etc.) peuvent retourner :

- des objets **Pydantic** (défaut)
- des **dictionnaires**
- des **DataFrames Pandas**

Exemple :

```python
client.list_movies(limit=10, output_format="dict")
client.list_ratings(limit=10, output_format="pandas")
```

---

## Tester en local

Vous pouvez aussi utiliser une API locale :

```python
config = MovieConfig(movie_base_url="http://localhost:8000")
client = MovieClient(config=config)
```

---

## Public cible

- Data Analysts
- Data Scientists
- Étudiants et curieux en Data
- Développeurs Python

---

## Licence

MIT License

---

## Liens utiles

- API Render : [https://moovie-backend-i.onrender.com](https://moovie-backend-i.onrender.com)
- PyPI : [https://pypi.org/project/movieIsdk](https://pypi.org/project/movieIsdk)
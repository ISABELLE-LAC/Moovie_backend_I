# Utilise une image légère de Python 3.12 comme base
FROM python:3.12-slim 
# Définit le répertoire de travail dans le conteneur
 WORKDIR /app 
# Copie le fichier des dépendances dans le conteneur
 COPY requirements.txt . 
# Installe les dépendances Python sans mise en cache
 RUN pip install --no-cache-dir --upgrade -r requirements.txt  
# Copie tous les fichiers .py et le fichier .db dans le conteneur
 COPY . . 
# Lance le serveur Uvicorn pour exécuter l'API FastAPI
 CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
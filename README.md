\# Gestion de bibliothèque



Projet fil rouge du module d'ingénierie logicielle.



Application Python permettant de gérer un catalogue de livres.



Prérequis : Python 3.9 ou supérieur.



\## Auteurs



\- Nada

\- Israe



\## Exécution



```bash

python -m bibliotheque.main

```



\## Fonctionnalités



\- Ajout et recherche de livres

\- Recherche par titre, auteur et ISBN

\- Sauvegarde et chargement du catalogue au format JSON

\- Suppression d'un livre par ISBN



\## Installation (développement)



Créer un environnement virtuel :



```bash

python -m venv .venv

```



Activer l'environnement virtuel sous Windows (CMD) :



```cmd

.venv\\Scripts\\activate.bat

```



Installer les dépendances de développement :



```bash

pip install -r requirements-dev.txt

```



\## Tests



Exécuter tous les tests :



```bash

pytest

```



Mesurer la couverture du code :



```bash

pytest --cov=bibliotheque --cov-report=term-missing

```



\## Contribuer



Consultez \[CONTRIBUTING.md](CONTRIBUTING.md) avant d'ouvrir une pull request.


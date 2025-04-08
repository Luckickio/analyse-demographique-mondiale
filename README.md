# Analyse Démographique Mondiale

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Dash 3.0.0](https://img.shields.io/badge/Dash-3.0.0-brightgreen?logo=plotly&logoColor=white)
![Plotly 6.0.0](https://img.shields.io/badge/Plotly-6.0.0-orange?logo=plotly&logoColor=white)
![Pandas 2.2.3](https://img.shields.io/badge/Pandas-2.2.3-yellow?logo=pandas&logoColor=black)
![Docker Support](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)
![Langue: Français](https://img.shields.io/badge/Langue-Français-blueviolet)

Une application web interactive pour visualiser et analyser les tendances démographiques mondiales de 1960 à 2018. Cette application utilise Dash et Plotly pour créer des visualisations interactives des données de population mondiale.

## Fonctionnalités

- **Cartes Choroplèthes** : Visualisations interactives montrant les tendances démographiques sur une carte du monde
  - Taux de croissance de la population
  - Croissance absolue de la population avec échelle fixe
  - Population par pays avec échelle fixe
- **Comparaisons par pays** : Visualisations comparatives entre différents groupes de pays
  - Top 10 pays les plus peuplés
  - Pays du G7
  - Pays émergents
  - Russie post-URSS
  - Rwanda (impact du génocide)
  - Pays en déclin ou stagnation démographique
- **Analyse continentale** : Visualisations par continent
  - Évolution de la population par continent
  - Nombre de pays par continent
- **Tendances mondiales** : Visualisations des tendances démographiques globales

  - Croissance moyenne de la population par année
  - Évolution de la population mondiale totale

- **Support en Français** : Interface en français avec traduction des noms de pays et de continents

## Installation

### Prérequis

- Python 3.10+
- pip (gestionnaire de paquets Python)

### Installation standard

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/Luckickio/analyse-demographique-mondiale.git
   cd analyse-demographique-mondiale
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Exécutez le script de traduction pour préparer les données (si countries_and_continents_fr.json est manquant) :

   ```bash
   python translate.py
   ```

4. Lancez l'application :

   ```bash
   python main.py
   ```

5. Ouvrez votre navigateur à l'adresse : `http://localhost:8050`

### Installation avec Docker

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/analyse-demographique-mondiale.git
   cd analyse-demographique-mondiale
   ```

2. Construisez et lancez le conteneur Docker :

   ```bash
   docker-compose up --build
   ```

3. Ouvrez votre navigateur à l'adresse : `http://localhost:8050`

## Structure du projet

```
analyse-demographique-mondiale/
├── assets/                  # Ressources statiques (CSS, images)
│   └── styles.css           # Feuille de style principale
├── callbacks/               # Callbacks Dash pour les interactions
│   ├── __init__.py          # Initialisation des callbacks
│   ├── choropleth.py        # Callbacks pour les cartes choroplèthes
│   ├── continents.py        # Callbacks pour l'analyse continentale
│   ├── countries.py         # Callbacks pour les comparaisons par pays
│   └── global_trends.py     # Callbacks pour les tendances mondiales
├── data/                    # Données sources
│   ├── countries_and_continents_fr.json  # Traductions FR des pays/continents
│   └── countries_population.csv          # Données de population
├── .dockerignore            # Fichiers à ignorer pour Docker
├── .gitignore               # Fichiers à ignorer pour Git
├── config.py                # Configuration de l'application
├── data_processing.py       # Traitement et préparation des données
├── docker-compose.yml       # Configuration Docker Compose
├── Dockerfile               # Configuration Docker
├── layouts.py               # Définition des layouts Dash
├── main.py                  # Point d'entrée de l'application
├── README.md                # Ce fichier
├── requirements.txt         # Dépendances Python
├── translate.py             # Script de traduction
├── translations.py          # Fonctions de gestion des traductions
└── utils.py                 # Fonctions utilitaires
```

## Technologies utilisées

- **[Dash](https://dash.plotly.com/)** : Framework Python pour la création d'applications web analytiques
- **[Plotly](https://plotly.com/python/)** : Bibliothèque de visualisation de données
- **[Pandas](https://pandas.pydata.org/)** : Manipulation et analyse de données
- **[pycountry](https://pypi.org/project/pycountry/)** : Gestion des informations sur les pays
- **[deep-translator](https://pypi.org/project/deep-translator/)** : Traduction automatique
- **[Docker](https://www.docker.com/)** : Conteneurisation de l'application

## Sources de données

Les données utilisées dans cette application proviennent du jeu de données “Country Population and Growth Rate Analysis” publié sur [Kaddle](https://www.kaggle.com/datasets/gauravkumar2525/country-population-and-growth-rate-analysis)

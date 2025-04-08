import os

PORT = int(os.getenv("PORT", 8050))

EXTERNAL_STYLESHEETS = ['assets/styles.css']

POPULATION_DATA_PATH = "data/countries_population.csv"
TRANSLATIONS_PATH = "data/countries_and_continents_fr.json"

MIN_YEAR = 1960
MAX_YEAR = 2018

CONTINENT_MAP = {
    "AF": "Africa",
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "OC": "Oceania",
    "SA": "South America"
}

G7_COUNTRIES = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]
EMERGING_COUNTRIES = ["China", "India", "Brazil", "South Africa", "Mexico"]
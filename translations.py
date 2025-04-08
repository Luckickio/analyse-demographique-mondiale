import json
from config import TRANSLATIONS_PATH

def load_translations():
    """
    Loads translations from the JSON file.

    Returns:
        tuple: Country translations, continent translations
    """
    try:
        with open(TRANSLATIONS_PATH, "r", encoding="utf-8") as f:
            translations = json.load(f)
            countries_fr = translations["countries"]
            continents_fr = translations["continents"]
        return countries_fr, continents_fr
    except Exception as e:
        print(f"Error loading translations: {e}")
        return {}, {}

def create_translation_maps(df, countries_fr, continents_fr):
    """
    Creates translation mappings for countries and continents.

    Args:
        df (DataFrame): DataFrame containing population data
        countries_fr (dict): Country translations
        continents_fr (dict): Continent translations

    Returns:
        tuple: Translation mappings for countries and continents
    """
    country_translation = {}
    for country in df["Country"].unique():
        country_translation[country] = countries_fr.get(country, country)

    continent_translation = {}
    for continent in df["Continent"].unique():
        continent_translation[continent] = continents_fr.get(continent, continent)
        
    return country_translation, continent_translation
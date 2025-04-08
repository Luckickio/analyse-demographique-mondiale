import pandas as pd
from utils import get_continent, generate_color
from translations import load_translations, create_translation_maps
from config import POPULATION_DATA_PATH, MIN_YEAR, MAX_YEAR

def load_and_process_data():
    """
    Loads and processes the population data.

    Returns:
        tuple: Complete DataFrame, cleaned DataFrame, timelapse DataFrame
    """
    df = pd.read_csv(POPULATION_DATA_PATH)
    
    df_clean = df.dropna(subset=['Population'])
    df_timelapse = df_clean[(df_clean["Year"] >= MIN_YEAR) & (df_clean["Year"] <= MAX_YEAR)]
    
    countries_fr, continents_fr = load_translations()
    
    df["Continent"] = df.apply(lambda row: get_continent(row["ISO3"], row["Country"]), axis=1)
    df = df[df["Continent"] != "Unknown"]
    
    country_translation, continent_translation = create_translation_maps(df, countries_fr, continents_fr)
    
    df["Country_FR"] = df["Country"].map(country_translation)
    df["Continent_FR"] = df["Continent"].map(continent_translation)
    
    df_clean["Country_FR"] = df_clean["Country"].map(country_translation)
    df_clean["Continent"] = df_clean.apply(lambda row: get_continent(row["ISO3"], row["Country"]) if "ISO3" in row else "Unknown", axis=1)
    df_clean["Continent_FR"] = df_clean["Continent"].map(lambda x: continent_translation.get(x, x))
    
    df_timelapse["Country_FR"] = df_timelapse["Country"].map(country_translation)
    df_timelapse["Continent"] = df_timelapse.apply(lambda row: get_continent(row["ISO3"], row["Country"]) if "ISO3" in row else "Unknown", axis=1)
    df_timelapse["Continent_FR"] = df_timelapse["Continent"].map(lambda x: continent_translation.get(x, x))
    
    country_color_map = {country: generate_color(country) for country in df["Country"].unique()}
    continent_color_map = {continent: generate_color(continent) for continent in df["Continent"].unique()}
    
    df.country_color_map = country_color_map
    df.continent_color_map = continent_color_map
    df.country_translation = country_translation
    df.continent_translation = continent_translation
    
    df_clean.country_color_map = country_color_map
    df_clean.continent_color_map = continent_color_map
    df_clean.country_translation = country_translation
    df_clean.continent_translation = continent_translation
    
    df_timelapse.country_color_map = country_color_map
    df_timelapse.continent_color_map = continent_color_map
    df_timelapse.country_translation = country_translation
    df_timelapse.continent_translation = continent_translation
    
    return df, df_clean, df_timelapse
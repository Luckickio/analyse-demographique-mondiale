import os
import pandas as pd
import pycountry
import pycountry_convert as pc
from deep_translator import GoogleTranslator
import json

json_file_path = "data/countries_and_continents_fr.json"
if not os.path.exists(json_file_path):
    df = pd.read_csv("data/countries_population.csv")
    df_clean = df.dropna(subset=['Population'])

    def get_continent(iso3, country_name):
        try:
            iso2 = pycountry.countries.get(alpha_3=iso3).alpha_2
            continent = pc.country_alpha2_to_continent_code(iso2)
            continent_map = {
                "AF": "Africa",
                "AS": "Asia",
                "EU": "Europe",
                "NA": "North America",
                "OC": "Oceania",
                "SA": "South America"
            }
            return continent_map.get(continent, "Unknown")
        except Exception:
            return "Unknown"

    df["Continent"] = df_clean.apply(lambda row: get_continent(row["ISO3"], row["Country"]), axis=1)

    country_names = df["Country"].unique()
    continent_names = df["Continent"].unique()

    translator = GoogleTranslator(source="auto", target="fr")
    country_dict = {}
    continent_dict = {}

    for country in country_names:
        try:
            country_dict[country] = translator.translate(country)
        except Exception as e:
            print(f"Error translating country {country}: {e}")
            country_dict[country] = country

    for continent in continent_names:
        try:
            continent_dict[continent] = translator.translate(continent)
        except Exception as e:
            print(f"Error translating continent {continent}: {e}")
            continent_dict[continent] = continent

    result = {
        "countries": country_dict,
        "continents": continent_dict
    }

    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("✅ Translations completed and saved in countries_and_continents_fr.json")
else:
    print("✅ Translation file already exists. Skipping translation.")

import hashlib
import pycountry
import pycountry_convert as pc
from config import CONTINENT_MAP

def get_continent(iso3, country_name=None):
    """
    Retrieves the continent of a country based on its ISO3 code.

    Args:
        iso3 (str): ISO3 code of the country
        country_name (str, optional): Name of the country (for debugging purposes)

    Returns:
        str: Name of the continent or "Unknown" in case of an error
    """
    try:
        if not iso3:
            return "Unknown"
        
        iso2 = pycountry.countries.get(alpha_3=iso3).alpha_2
        continent_code = pc.country_alpha2_to_continent_code(iso2)
        return CONTINENT_MAP.get(continent_code, "Unknown")
    except Exception:
        return "Unknown"

def generate_color(name):
    """
    Generates a unique color based on the hash of the given name.

    Args:
        name (str): Name used to generate the color

    Returns:
        str: Hexadecimal color code
    """
    return f'#{hashlib.md5(name.encode()).hexdigest()[:6]}'
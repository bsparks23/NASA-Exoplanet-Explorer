import requests
from openai import OpenAI
import os
import random


# Fetch data from the NASA Exoplanet TAP Service
def fetch_exoplanet_data():
    base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    query = "select pl_name,pl_orbper,pl_orbsmax,pl_radj,pl_eqt,pl_masse from ps&format=json"
    # For earth sized planets - "select pl_name,pl_orbper,pl_orbsmax,pl_radj,pl_eqt,pl_masse,dec+from+ps+where+upper(soltype)+like+'%CONF%'+and+pl_masse+between+0.5+and+2.0"
    url = base_url + query
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from NASA Exoplanets TAP service.")
        return None

# Generate a story based on exoplanet data
def generate_story(exoplanet_data):
    random_exoplanet = random.choice(exoplanet_data)

    # Extract data
    planet_name = random_exoplanet["pl_name"]
    orbital_period = random_exoplanet["pl_orbper"]
    semi_major_axis = random_exoplanet["pl_orbsmax"]
    planet_radius = random_exoplanet["pl_radj"]
    equilibrium_temperature = random_exoplanet["pl_eqt"]
    planet_size = random_exoplanet["pl_masse"]
    
    prompt = f"Tell me a story about the exoplanet {planet_name}. It has an orbital period of {orbital_period} days, a semi-major axis of {semi_major_axis} AU, a radius of {planet_radius} Jupiter radii, a planet size of {planet_size} earth mass, and an equilibrium temperature of {equilibrium_temperature} K. If any values are None, please leave that part of the story out."

    client = OpenAI(
        api_key = os.environ.get("ReplaceHere"),
    )
    completion = client.chat.completions.create(
        messages = [{"role": "user", "content": prompt}],
        model = "gpt-3.5-turbo",
        max_tokens = 250,
    )

    story = completion.choices[0].message.content
    return planet_name, story


def main():
    exoplanet_data = fetch_exoplanet_data()
    if exoplanet_data:
        planet_name, story = generate_story(exoplanet_data)
        print(f"Exoplanet {planet_name}:")
        print(story)
    else:
        print("Something went wrong. Please check that there is data to parse.")


if __name__ == "__main__":
    main()
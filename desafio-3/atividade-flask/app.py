from flask import Flask, render_template
import urllib.request, json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context #Para não dar erro de certificado

app = Flask(__name__)

@app.route('/')
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    characters_dict = json.loads(data)

    return render_template("characters.html", characters=characters_dict["results"])

@app.route("/profile/<int:id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    profile_dict = json.loads(data)

    # Informações de origem
    origin_url = profile_dict["origin"]["url"]
    origin_response = urllib.request.urlopen(origin_url)
    origin_data = origin_response.read()
    origin_dict = json.loads(origin_data)

    # Informações de localização
    location_url = profile_dict["location"]["url"]
    location_response = urllib.request.urlopen(location_url)
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    return render_template("profile.html", profile=profile_dict, origin=origin_dict, location=location_dict)

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters_data = response.read()
    characters_dict = json.loads(characters_data)

    characters_list = []

    for character in characters_dict["results"]:
        character_info = {
            "name": character["name"],
            "status": character["status"]
        }
        characters_list.append(character_info)
    
    return {"characters": characters_list}

@app.route("/locations")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations_data = response.read()
    locations_dict = json.loads(locations_data)

    locations_list = locations_dict["results"]
    
    return render_template("locations.html", locations=locations_list)

@app.route("/location_profile/<int:id>")
def get_location_profile(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    location_data = response.read()
    location_dict = json.loads(location_data)

    return render_template("location_profile.html", location=location_dict)

@app.route("/episodes")
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes_data = response.read()
    episodes_dict = json.loads(episodes_data)

    episodes_list = episodes_dict["results"]
    
    return render_template("episodes.html", episodes=episodes_list)

@app.route("/episode_profile/<int:id>")
def get_episode_profile(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    episode_data = response.read()
    episode_dict = json.loads(episode_data)

    return render_template("episode_profile.html", episode=episode_dict)


@app.route("/location/<int:id>")
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    location_data = response.read()
    location_dict = json.loads(location_data)

    # Obter a lista de personagens associados a esta localização
    characters = []
    for resident in location_dict["residents"]:
        response = urllib.request.urlopen(resident)
        character_data = response.read()
        character_dict = json.loads(character_data)
        characters.append(character_dict)

    return render_template("location.html", location=location_dict, characters=characters)

@app.route("/episode/<int:id>")
def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    episode_data = response.read()
    episode_dict = json.loads(episode_data)

    # Obter a lista de personagens associados a este episódio
    characters = []
    for character_url in episode_dict["characters"]:
        response = urllib.request.urlopen(character_url)
        character_data = response.read()
        character_dict = json.loads(character_data)
        characters.append(character_dict)

    return render_template("episode.html", episode=episode_dict, characters=characters)



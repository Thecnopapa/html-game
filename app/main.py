from flask import Flask, render_template, request, url_for, send_file
import requests
import pandas as pd
import os
import json
import random
from PIL import Image
import io
app = Flask(__name__, template_folder='game/templates', static_folder='game')



@app.route("/style/<file>")
def return_style(file):
    return app.send_static_file("style/" + file)

@app.route("/scripts/<file>")
def return_scripts(file):
    return app.send_static_file("scripts/" + file)


@app.route("/")
def index():
    return render_template("main-menu.html")

@app.route("/rpg-test")
def rpg_test():
    return render_template("rpg-base.html")

@app.post("/rpg/map")
def get_rpg_map():
    r = request.get_json()
    map_name = r["mapName"]
    print("Fetching map: " + map_name)
    print(os.getcwd())
    map_df = pd.read_csv(os.path.join("app/game/rpg-maps", map_name + ".csv"), header=None)
    print(map_df)
    texture_df = map_df.map(get_tile_url)
    print(texture_df)
    map_data = {
        "mapName": map_name,
        "tileTextures": texture_df.to_dict(orient="list"),
        "size": map_df.shape,
    }
    return json.dumps(map_data)


@app.route("/rpg/tile/<path:path>", methods=["GET", "POST"])
def return_tile(path):
    print(path)

    modifiers = request.args.get("modifiers")
    if modifiers != "":
        modifiers = modifiers.split(";")

    print(request.args.get("modifiers"))
    tile_path = os.path.join("app/game/rpg-assets/tiles/", path)
    print("TILE PATH:", tile_path)
    img = Image.open(tile_path).convert("RGBA")
    print("MODIFIERS", modifiers)
    if len(modifiers) > 0:
        for modifier in modifiers:
            modifier_components = modifier.split("-")
            modifier_name = "-".join(modifier_components[2:])
            modifier_tile = [f for f in os.listdir("app/game/rpg-assets/tiles/{}/{}/".format(modifier_components[0], modifier_components[1])) if modifier_name in f][0]
            modifier_path = "app/game/rpg-assets/tiles/{}/{}/{}".format(modifier_components[0], modifier_components[1], modifier_tile)
            modifier_img = Image.open(modifier_path).convert("RGBA")
            img.paste(modifier_img, (0, 0), modifier_img)
    b = io.BytesIO()
    img.save(b, "png")
    b.seek(0)
    return send_file(b, mimetype="image/png")


def get_tile_url(tile):
    try:
        modifiers = ""
        if "$" in tile:
            modifiers = tile.split("$")[1]
            tile = tile.split("$")[0]
        components = tile.split("-")
        tile_name = "-".join(components[2:])
        #print(tile)
        available_tiles = os.listdir("app/game/rpg-assets/tiles/{}/{}/".format(components[0], components[1]))
        #print(available_tiles, tile_name)
        target_tiles = [t for t in available_tiles if tile_name in t]
        #print(target_tiles)
        if len(target_tiles) == 0:
            return "No tile"
        r_tile = random.choice(target_tiles)
        tile_url = "/rpg/tile/{}/{}/{}?modifiers={}".format(components[0], components[1], r_tile, modifiers)
        #print(tile_url)
        return tile_url
    except:
        return "Error"



def main():
    app.run(port=5000, host="0.0.0.0", debug=True) # Not used if run from bash

if __name__ == "__main__":
    main()
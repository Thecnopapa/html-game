from flask import Flask, render_template, request
import requests
import pandas as pd
import os
import json
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
    map_data = {
        "mapName": map_name,
        "mapTiles": map_df.to_dict(orient="list"),
        "size": map_df.shape
    }
    return json.dumps(map_data)





def main():
    app.run(port=4242, host="0.0.0.0", debug=True) # Not used if run from bash

if __name__ == "__main__":
    main()
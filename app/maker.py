from flask import Flask, render_template, request, url_for, send_file
import requests
import pandas as pd
import os
import json
import random
from PIL import Image
import io
app = Flask(__name__, template_folder='maker/templates', static_folder='maker')


SIZE = 32


@app.route("/style/<file>")
def return_style(file):
    return app.send_static_file("style/" + file)

@app.route("/scripts/<file>")
def return_scripts(file):
    return app.send_static_file("scripts/" + file)

@app.route("/")
def index():
    return render_template("maker-menu.html")

@app.route("/editor/<style>/<asset>")
def open_editor(style, asset):
    return render_template("editor-{}-{}.html".format(style, asset))

















def main():
    app.run(port=4242, host="0.0.0.0", debug=True) # Not used if run from bash

if __name__ == "__main__":
    main()
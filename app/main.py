from flask import Flask, render_template
app = Flask(__name__, template_folder='game/templates')


@app.route("/")
def index():
    return render_template("main-menu.html")






def main():
    app.run(port=4242, host="0.0.0.0", debug=True) # Not used if run from bash

if __name__ == "__main__":
    main()
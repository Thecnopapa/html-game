from flask import Flask

app = Flask(__name__)


def main():
    app.run(port=4242, host="0.0.0.0", debug=True) # Not used if run from bash

if __name__ == "__main__":
    main()
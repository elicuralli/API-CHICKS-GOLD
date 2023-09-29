from flask import Flask,jsonify
from routes import gallons


app = Flask(__name__)


if __name__ == "__main__":
    #register blueprints
    app.register_blueprint(gallons.gallon,url_prefix = '/api/gallons')

    app.run()
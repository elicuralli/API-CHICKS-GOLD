from flask import Flask
from routes.gallons import gallon


#initialize flask object
app = Flask(__name__)


if __name__ == "__main__":
    #register blueprints
    app.register_blueprint(gallon, url_prefix = '/gallon')

    app.run(debug=True)
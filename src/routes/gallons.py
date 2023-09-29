from flask import Flask,request,jsonify,Blueprint
from model.functions import Actions_Gallon

gallon = Blueprint('gallon_blueprint',__name__)

@gallon.route('/ask_values', methods = ['POST'])
def ask_values():

#the user enters the values for X,Y,Z and i process them as a json request to return a dictionary
    try:

        x_level = request.json['x level']
        y_level = request.json['y level']
        z_measure = request.json['z measurement']

        if(z_measure > x_level or z_measure > y_level):
            return jsonify({"error": " Z exceeds maximum capacity for X or Y"}),400
        
        else:
            if x_level > y_level:
                gallon = Actions_Gallon.fill(y_level)
            else: 
                gallon = Actions_Gallon.fill(x_level)
        
        return jsonify({"ok":True,"status":200,"data":{"message":gallon}})
    

    except Exception as ex:
        return jsonify({"ok":False,"status": 500,"data":{"message": str(ex)}})

#@gallon.route('/')
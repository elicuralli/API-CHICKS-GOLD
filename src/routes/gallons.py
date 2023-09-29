from flask import Flask,request,jsonify,Blueprint
from model.functions import Actions_Gallon

gallon = Blueprint('gallon_blueprint',__name__)

@gallon.route('/ask_values', methods = ['POST'])
def ask_values():

#the user enters the values for X,Y,Z and i process them as a json request to return a dictionary
    try:

        x_level_str = request.json['x level']
        y_level_str = request.json['y level']
        z_measure_str = request.json['z measurement']

        # check is values are integer with isdigit()
        if not x_level_str.isdigit() or not y_level_str.isdigit() or not z_measure_str.isdigit():
            return jsonify({"error": "values must be integers"}), 400

        # convert string to integers
        x_level = int(x_level_str)
        y_level = int(y_level_str)
        z_measure = int(z_measure_str)

        gallon_manager = Actions_Gallon(x_level,y_level)

        """if z_measure> x_level+y_level:
            return jsonify({"error": "Z exceeds maximum capacity for X or Y"}), 400
        """
        
        if z_measure> x_level or z_measure >y_level:
            return jsonify({"error": "There's no solution Z exceeds maximum capacity for X or Y "}), 400
        
    # Call existing is_z_reached function to perform the remaining operations

        x_level, y_level = gallon_manager.is_z_reached(z_measure)

        return jsonify({"ok": True, "status": 200, "data": {"message": "Z has been reached", "x_level": x_level, "y_level": y_level}})

    except Exception as ex:
        return jsonify({"ok":False,"status": 500,"data":{"message": str(ex)}})

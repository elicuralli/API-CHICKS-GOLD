from flask import request,jsonify,Blueprint
from model.functions import Actions_Gallon

gallon = Blueprint('gallon_blueprint',__name__)

@gallon.route('/add_values', methods = ['POST'])
def add_values():

#the user enters the values for X,Y,Z and i process them as a json request to return a dictionary
    try:
        
        x_level_str = request.json['x_level']
        y_level_str = request.json['y_level']
        z_measure_str = request.json['z_measurement']
       

        # check is values are integer with isdigit()
        if not x_level_str.isdigit() or not y_level_str.isdigit() or not z_measure_str.isdigit():
            return jsonify({"error": "values must be integers"}), 400

        # convert string to integers
        x_level = int(x_level_str)
        y_level = int(y_level_str)
        z_measure = int(z_measure_str)
        
        #calculate which one has less capacity 
        menor = min(x_level,y_level)

        if  menor > z_measure:
            return jsonify({"error": "There's no solution  X and Y exceed Z "}), 400
        
        if z_measure> x_level and z_measure>y_level:
            return jsonify({"error": "There's no solution Z is greater than X and Y"})

        gallon_manager = Actions_Gallon(x_level,y_level)

    #check if z reached with the function created 
        x_level, y_level = gallon_manager.is_z_reached(z_measure)

        result = {
            "ok": True,
            "status": 200,
            "data": {
                "message": "Z has been reached",
                "x_level": x_level,
                "y_level": y_level
            }
        }

        return jsonify(result)

    except Exception as ex:
        result = {
            "ok": False,
            "status": 500,
            "data": {
                "message": str(ex)
            }
        }
        return jsonify(result), 500 
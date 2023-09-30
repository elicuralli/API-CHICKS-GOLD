            **WATER JUG CHALLENGE**

DESCRIPTION:

    This project implements a solution to fill gallons of water until Z is reached
using two gallons with diferent capacities. A web API is provied using Flask that 
allows users to specify initial water levels in gallons and the desired Z measurement

CONTENT TABLE:

    -instalation
    -main functions
    -examples

INSTALATION: using windows

1. create virtual environment 
    python -m venv venv

2. activate using the command
    venv\Scripts\activate

3. copy the requirements.txt using
    pip install -r requirements.txt

4. run the project 
    cd src then run python app.py


USE

you can interact with the API using HTTP POST requests to  '/gallon/add_values' path.
you must send a JSON body with the initial levels of x_level,y_level and z_measurement. 
The API will calculate if it is posible to reach Z measurement and it will return the gallon
level after performing the operations

example:

json request:

{
  "x_level": "2",
  "y_level": "10",
  "z_measurement": "4"
}

expected json response:
{
  "ok": true,
  "status": 200,
  "data": {
    "message": "Z has been reached",
    "x_level": 0,
    "y_level": 4
  }
}

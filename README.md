# 💦**WATER JUG CHALLENGE**💦


## **DESCRIPTION**

This project implements a solution to fill gallons of water until Z is reached
using two gallons with diferent capacities. A web API is provied using Flask that 
allows users to specify initial water levels in gallons and the desired Z measurement

## **CONTENT TABLE:**

- Instalation
- Main Function
- Examples


## **INSTALATION: using windows**

1. create virtual environment 
    ```python -m venv venv```

2. activate using the command
    ```venv\Scripts\activate```

3. copy the requirements.txt using
    ```pip install -r requirements.txt```

4. run the project 
    ```cd src then run python app.py```

## **FUNCTIONS**


### Create the class to define the functions that we need: fill,transfer, is_z_reached
```
class Actions_Gallon():
    def __init__(self,x_capacity,y_capacity):
        self.x_capacity = x_capacity
        self.y_capacity = y_capacity
        self.x_level = 0
        self.y_level = 0
```
    def fill(self,gallon):
        
        # we fill the specified bucket until its maximum capacity
        if gallon =="x":
            self.x_level = self.x_capacity
        elif gallon =="y":
            self.y_level = self.y_capacity

    def transfer(self,source,target,amount):
        #transfer water from the source gallon to the target gallon

        if source == "x" and target == "y":

            if self.x_level >= amount:
                self.x_level -= amount
                self.y_level += amount
            else:
                self.y_level += self.x_level
                self.x_level = 0

        elif source == "y" and target == "x":
            # Transfiere desde y a x
            if self.y_level >= amount:
                self.y_level -= amount
                self.x_level += amount
            else:
                self.x_level += self.y_level
                self.y_level = 0
  
    def is_z_reached(self, z_measure):

        #check level of water in the gallons to define source and target

        if self.x_level < self.y_level:
            source = 'x'
            target = 'y'
        else:
            source = 'y'
            target = 'x'

        #we use a while cicle to check is Z reached or not, repeating the process in every iteration
        while self.x_level != z_measure and self.y_level != z_measure:
            
            #Check if it is possible to continue filling and transferring 
            if (self.x_level == self.x_capacity and self.y_level == self.y_capacity) or (self.x_level == 0 and self.y_level == 0):
                break

            # Calculate how much water can be added without exceeding z
            remaining_space_x = z_measure - self.x_level
            remaining_space_y = z_measure - self.y_level

            # Fill the gallon with less capacity without exceeding z
            if source == 'x':
                if self.y_level + self.x_level <= z_measure:
                    self.transfer(source, target, remaining_space_x)
                    self.fill(source, remaining_space_x)
                else:
                    break
            else:
                if self.x_level + self.y_level <= z_measure:
                    self.transfer(source, target, remaining_space_y)
                    self.fill(source, remaining_space_y)
                else:
                    break

        return self.x_level, self.y_level
        
## **Explanation**
- __init__(self, x_capacity, y_capacity): This is the constructor of the class that initializes the levels and capacities of the two gallons x and y.
- __fill__(self, gallon): This method fills the specified gallon to its maximum capacity (x_capacity or y_capacity)
- __transfer__(self, source, target, amount): This method transfers a specific amount of water from the source gallon to the target gallon, ensuring that no gallon's capacity is exceeded.
- __is_z_reached__(self, z_measure): This is the main method that attempts to fill the gallons until measurement Z is reached in one of the gallons. It uses a while loop that repeats the filling and transferring of water until certain conditions are met indicating that Z has been reached in one of the gallons or that further filling and transferring is no longer possible.

  
## **USE**

you can interact with the API using HTTP POST requests to  ```'/gallon/add_values'``` path.
you must send a JSON body with the initial levels of x_level,y_level and z_measurement. 
The API will calculate if it is posible to reach Z measurement and it will return the gallon
level after performing the operations

**example:**

json request:
```
{
  "x_level": "2",
  "y_level": "10",
  "z_measurement": "4"
}
```
**expected json response:**
```
{
  "ok": true,
  "status": 200,
  "data": {
    "message": "Z has been reached",
    "x_level": 0,
    "y_level": 4
  }
}
```
#### Just in case the values for Z provided from the user are greater than the expect it 
```
{
  "error": "There's no solution Z is greater than X and Y"
}
```
#### when X and Y exceed Z

```
{
  "error": "There's no solution  X and Y exceed Z "
}
```

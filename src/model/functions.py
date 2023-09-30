#create the class to define the functions that we need
#fill,empty,transfer 

class Actions_Gallon():
    
    def __init__(self,x_capacity,y_capacity):
        self.x_capacity = x_capacity
        self.y_capacity = y_capacity
        self.x_level = 0
        self.y_level = 0

    
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

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
    
    def empty(self,gallon):
        #empty the specified gallon completely 
        
        if gallon =="x":
            self.x_level = 0
        elif gallon =="y":
            self.y_level = 0
    
    def transfer(self,source,target):
        #transfer water from the source gallon to the target gallon
        
        max_transfer = min(self.x_level if source == 'x' else self.y_level,
                       self.y_capacity - (self.x_level if target == 'x' else self.y_level)) #this operation define how much water we can transfer 
        
        #update water level
        
        if source =='x':
            self.x_level -= max_transfer
        else:
            self.y_level -= max_transfer

        if target =='x':
            self.x_level += max_transfer
        else:
            self.y_level += max_transfer
    
    def is_z_reached(self,z_measure):

        #fill, empty,transfer gallons, until z is reached or until it is not posible continue
        
        while self.x_level + self.y_level != z_measure:

            #verify z is reached or not in every cicle
            if self.x_level+self.y_level == z_measure:
                break

            #find gallon with less capacity to fill
            if self.x_level < self.y_level:
                source = 'x'
                target = 'y'
            else:
                source = 'y'
                target = 'x'
            
            #fill gallon with less capacity
            self.fill(source)

            #transfer water to the target gallon
            self.transfer(source,target)

            #empty source gallon
            self.empty(source)

            #verify z is reached or not in every cicle
            if self.x_level+self.y_level == z_measure:
                break
        
        #here return level water in every gallon
        return self.x_level, self.y_level
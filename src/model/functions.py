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
        
    
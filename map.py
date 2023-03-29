## Define map cells
# Base class for map cells
class BaseCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro(self):
        pass

    def action(self):
        pass

# Spawn point map cell
class StartCell(BaseCell):
    def intro(self):
        return """
        You awake on a narrow beach with on one side the far-stretched ocean and on the other side a dense array of trees.
        Although you are still dull from your long sleep, you try to figure out what to do and where to go.
        One thing is sure, you need to get home as quick as possible, since this is not where you should be.
        You mark this beach by drawing a massive "X" in the sand, and off you go! 
        """
    
    def action(self):
        pass

# 2-way forest map cell
class ForestCell2(BaseCell):
    def intro(self):
        return """
        You find yourself in an area with nothing more to see than trees and a narrow path.
        Nothing much to see and do here, apart from moving on.
        """
    
    def action(self):
        pass

# 3-way forest map cell
class ForestCell3(BaseCell):
    def intro(self):
        return """
        3-way crossing in the forest
        """
    
    def action(self):
        pass

# 4-way forest map cell
class ForestCell4(BaseCell):
    def intro(self):
        return """
        4-way crossing in the forest
        """
    
    def action(self):
        pass

## Define map
map = [[],[],[]]
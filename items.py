## Define master Item() class
class Item:
    # Constructor
    def __init__(self, name, description):
        self.name
        self.description

    def __str__(self):
        return "{NAME}:\n\t{DESCRIPTION}".format(NAME=self.name, DESCRIPTION=self.description)
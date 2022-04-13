class Location: 
locName = ""
locHasMonsters = False 
locHasItems = False 
locGet = ["placeholder1", "placeholder2"]
locGo = ["placeholder3", "placeholder4", "placeholder5"]
locFlavor = ""

def __init__(self):
    self.locName = "test"
    self.locHasMonsters = True
    self.locHasItems = True
    self.locGet[0] = "a location"
    self.locGet[1] = "another location"
    self.locGo[0] = "a new place"
    self.locGo[1] = "a different place"
    self.locGo[2] = "a third place! wowee!"
    self.locFlavor = "bitter, with notes of cellulose and TV static"

def travel(self, locGo, locGet):

    return self.locName;
    

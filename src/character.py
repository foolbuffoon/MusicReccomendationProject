#
class Character:
    playerHealth = 0
    playerInventorySpace = 0
    playerInventory = []
    victory = False
    playerMoney = 0
    alive = True

    def __init__(self):
        self.playerHealth = 100
        self.playerInventorySpace = 10
        self.playerInventory = []
        self.victory = False
        self.playerMoney = 0
        self.alive = True

class Character:
    player_health = 0
    PLAYER_INVENTORY_SPACE = 0
    player_inventory = []
    victory = False
    player_money = 0
    alive = True

    def __init__(self):
        self.player_health = 100
        self.PLAYER_INVENTORY_SPACE = 10
        self.player_inventory = []
        self.victory = False
        self.player_money = 0
        self.alive = True

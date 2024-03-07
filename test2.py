class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y


player = Player(6, 8)

attributes = ["x", "y"]

# del player.x

for i in attributes:
    delattr(player, i)

print(player.y)

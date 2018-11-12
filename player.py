# The ultimate player python file
import random
from file import CustomFile

class Player:
    # Setting globals.
    global playerName, playerClass, playerLevel, playerMaxHealth, playerCurrentHealth, playerMaxMana, playerCurrentMana

    # Spawn the player. Give him all the basics of everything.
    # We'll use kwargs with the player since there will be only one instance of the class, and they can be flexible.
    def __init__(self, **kwargs):
        self.playerName = kwargs.get("playerName")
        self.playerClass = kwargs.get("playerClass")
        self.playerLevel = kwargs.get("playerLevel")
        self.playerMaxHealth = kwargs.get("playerMaxHealth")
        self.playerCurrentHealth = kwargs.get("playerCurrentHealth")
        self.playerMaxMana = kwargs.get("playerMaxMana")
        self.playerCurrentMana = kwargs.get("playerCurrentMana")

    def createPlayer(self):
        # if the player doesn't choose a class.
        player_classes = CustomFile.readFileToObj("class_names.txt")
        if self.playerClass == None: self.playerClass = player_classes[random.randrange(0, len(player_classes))]
        self.playerName = input('Creating character. What shall be your name?\n')
        print(self.playerName, 'the human', self.playerClass, 'has been born. Long live the cause!')

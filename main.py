import world
import playerInput
from player import Player

global playerobj

def cartographerEnterPoint():
    world.__generateWorld(True)
    world.__populateWorld(1000, True)
    playerobj = Player(playerName="Justin", playerLevel=1, playerMaxHealth=100, playerCurrentHealth=100, playerMaxMana=100, playerCurrentMana=100)
    playerobj.createPlayer()
    playerInput.passPlayerObject(playerobj)
    #world.__simulateHistory(False)

cartographerEnterPoint()
playerInput.primitivePlayerInput()

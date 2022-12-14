from GetChoice import getChoice
from Combat import startCombat
from enemies.FireFox import FireFox


def Forest(gameState):
    print("You are in the forest.")
    choices=["Go to Water front (1)","Go to Large Field (6)","Go to Spider Field (4)","Go to Pond (3)","Save Game"]
    
    if gameState.playerLevel <= 4 and gameState.playerLevel >= 3:
        print("You see a massive fox. Its fur is shimmering with glowing embers.")
        choices.append("Attack the fox")
    
    print("What would you like to do?")
    choice = getChoice(choices)
    match choice:
        case "Attack the fox":
            firefox = FireFox()
            startCombat(gameState,firefox)
        case "Go to Water front (1)":
            gameState.currentLocationID = 1
        case "Go to Large Field (6)":
            gameState.currentLocationID = 6
        case "Go to Spider Field (4)":
            gameState.currentLocationID = 4
        case "Go to Pond (3)":
            gameState.currentLocationID = 3
        case "Save Game":
            gameState.printSaveCode()
            Forest(gameState)
        case _:
            print("Invalid choice")
            Forest(gameState)
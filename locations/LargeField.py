from GetChoice import getChoice
from Combat import startCombat
from enemies.SmallPig import SmallPig

def LargeField(gameState):
    print("You are in the large field.")
    choices=["Go to Water front (1)","Go to Forest (2)", "Go to Spider Field (4)","Go to Dunes (5)","Save Game"]

    if gameState.playerLevel <= 3:
        print("You see an angry pig, looking for a fight.")
        choices.append("Attack the pig")
        
    print("What would you like to do?")
    choice = getChoice(choices)
    match choice:
        case "Attack the pig":
            smallPig = SmallPig()
            startCombat(gameState,smallPig)
        case "Go to Water front (1)":
            gameState.currentLocationID = 1
        case "Go to Forest (2)":
            gameState.currentLocationID = 2
        case "Go to Spider Field (4)":
            gameState.currentLocationID = 4
        case "Go to Dunes (5)":
            gameState.currentLocationID = 5
        case "Save Game":
            gameState.printSaveCode()
            LargeField(gameState)
        case _:
            print("Invalid choice")
            LargeField(gameState)



from simple_term_menu import TerminalMenu

from GameState import GameState


def getChoice(choiceArray):
    terminal_menu = TerminalMenu(choiceArray)
    menu_entry_index = terminal_menu.show()
    print("You selected: " + choiceArray[menu_entry_index])
    return choiceArray[menu_entry_index]



def createCharacter():
    print("What is your name? (no more than 10 characters)")
    playerName = input()
    if len(playerName) > 10:
        print("Name too long")
        createCharacter()
    else:
        return playerName
    

def main():
    print("Welcome!\n")
    match getChoice(["New Game", "Continue Game"]):
        case "New Game":
            gameState = GameState()
            gameState.printSaveCode()
        case "Continue Game":
            print("Enter your save code:")
            saveCode = input()
            gameState = GameState(saveCode)
main()
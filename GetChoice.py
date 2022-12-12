from simple_term_menu import TerminalMenu

def getChoice(choiceArray):
    terminal_menu = TerminalMenu(choiceArray)
    menu_entry_index = terminal_menu.show()
    print("You selected: " + choiceArray[menu_entry_index])
    return choiceArray[menu_entry_index]
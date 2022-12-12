from GetChoice import getChoice

def startCombat(gamestate,enemy):
    print("You ready your weapon and prepare to fight.")

    availableActions = ["Attack With Sword (5 DMG)", "Check","Dodge", "Use Health Potion (+30 HP)"]

    if gamestate.playerLevel >=3:
        availableActions = ["Attack With Sword (5 DMG)","Block", "Check","Dodge", "Use Health Potion (+30 HP)"]
    if gamestate.playerLevel >=6:
        availableActionsSword = ["Attack With Sword (5 DMG)","Block", "Enter axe mode", "Check","Dodge", "Use Health Potion (+30 HP)"]
        availableActionsAxe = ["Attack With Axe (10 DMG)", "Enter sword mode", "Check","Dodge", "Use Health Potion (+30 HP)"]
        availableActions = availableActionsSword

    enemyPerformsActionThisRound = False
    while True:

        #player action
        print("What would you like to do?")
        playerChoice = getChoice(availableActions)
        match playerChoice:
            case "Attack With Sword (5 DMG)":
                print("You attack the enemy for 5 damage")
                enemy.health -= 5
            case "Attack With Axe (10 DMG)":
                print("You attack the enemy for 10 damage")
                enemy.health -= 10
            case "Block":
                print("You hold your shield up")
            case "Enter axe mode":
                availableActions = availableActionsAxe
                print("You attach your sword to your shield and enter axe mode")
            case "Enter sword mode":
                availableActions = availableActionsSword
                print("You detach your sword from your shield and enter sword mode")
            case "Check":
                print("You have "+str(gamestate.playerHealth)+" health")
                print("The enemy has "+str(enemy.health)+" health")
                print("the enemy intends to perform "+enemy.getIntent())
            case "Dodge":
                print("You dodge to the side")
            case "Use Health Potion (+30 HP)":
                if gamestate.healthPotionCount > 0:
                    gamestate.healthPotionCount -= 1
                    gamestate.playerHealth += 30
                    if gamestate.playerHealth > 100:
                        gamestate.playerHealth = 100
                    print("You use a health potion")
                    print("You have "+str(gamestate.healthPotionCount)+" health potions left")
                    print("You have "+str(gamestate.playerHealth)+" health")
                else:
                    print("You don't have any health potions")
            case _:
                print("Invalid choice")
            
        if(enemy.health <= 0):
            enemy.giveReward(gamestate)
            break

        #enemy action
        if enemyPerformsActionThisRound:
            enemyPerformsActionThisRound = False
            gamestate.playerHealth-=enemy.attack(playerChoice)
        else:
            enemyPerformsActionThisRound = True
    
            
            
        
        

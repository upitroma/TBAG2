from GetChoice import getChoice

def startCombat(gamestate,enemy):
    print("You ready your weapon and prepare to fight.")

    enemyPerformsActionThisRound = False

    while True:

        #player action
        print("What would you like to do?")
        playerChoice = getChoice(["Attack With Sword (5 DMG)", "Check","Dodge", "Use Health Potion (+30 HP)"])
        match playerChoice:
            case "Attack With Sword (5 DMG)":
                print("You attack the enemy for 5 damage")
                enemy.health -= 5
            case "Check":
                print("You have "+str(gamestate.playerHealth)+" health")
                print("The enemy has "+str(enemy.health)+" health")
                print("the enemy intends to perform "+enemy.getIntent())
            case "Dodge":
                print("You dodge to the side")
            case "Use Health Potion":
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
    
            
            
        
        

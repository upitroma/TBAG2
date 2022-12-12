import random
class SmallPig:
    
    def __init__(self):
        self.rng = random.Random()
        self.health = 50
        self.locationID = 2
        self.attackOptions=["do nothing","headbutt","windup"]
        self.intent="unknown"

    def getIntent(self):
        if self.intent=="unknown":
            self.intent = random.choice(self.attackOptions)
            return self.intent
        else:
            return self.intent
    
    def attack(self,playerAction):
        if self.intent=="unknown":
            self.intent = random.choice(self.attackOptions)
        
        match self.intent:
            case "headbutt":
                self.intent="unknown"
                if playerAction=="Block":
                    print("The pig headbutts your shield, hurting itself for 3 damage")
                    self.health -= 3
                    return 0
                elif playerAction != "Dodge":
                    print("The pig headbutts you for 5 damage")
                    return 5
                return 0
            case "windup":
                print("The pig winds up for a charge")
                self.intent="charge"
                return 0
            case "charge":
                self.intent="unknown"
                if playerAction=="Block":
                    print("The pig impacts your shield for 5 damage")
                    return 5
                elif playerAction=="Dodge":
                    return 0
                else:
                    print("The pig charges you for 15 damage")
                    return 15
            case "do nothing":
                print("The pig does nothing")
                self.intent="unknown"
                return 0
            case _:
                print("The pig does nothing")
                return 0
    
    def giveReward(self,gameState):
        print()
        gameState.healthPotionCount += 1
        if gameState.healthPotionCount > 8:
            gameState.healthPotionCount = 8
        print("You have defeated the pig")
        print("You gain 1 health potion")
        print()
        gameState.levelUp()
        print("Press enter to continue")
        input()


        

    

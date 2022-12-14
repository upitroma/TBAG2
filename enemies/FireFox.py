import random
class FireFox:
    def __init__(self):
        self.health = 100
        self.locationID = 2
        self.attackOptions=["do nothing","triple claw slash","fireball","windup"]
        self.intent="unknown"
        self.tripleClawSlashCount = 0
    
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
            case "triple claw slash":
                if self.tripleClawSlashCount == 3:
                    self.intent="do nothing"
                    self.tripleClawSlashCount = 0
                if playerAction=="Block":
                    print("The Fire Fox slashes your shield for 1 damage")
                    return 1

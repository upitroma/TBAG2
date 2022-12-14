import binascii
from hashlib import sha256

SERVER_SECRET="some random secret"


def createCharacter():
    print("What is your name? (no more than 10 characters)")
    playerName = input()
    if len(playerName) > 10:
        print("Name too long")
        createCharacter()
    else:
        return playerName

class GameState:
    def __init__(self,saveCode=None):
        if saveCode == None:
            self.validGameState = True
            self.playerName = createCharacter() # 10 char 2^80
            self.playerLevel = 1 # max 16 2^4
            self.playerHealth = 100 # max 1024 2^10
            self.currentLocationID = 0 # max 128 2^7
            self.healthPotionCount = 3 # max 8 2^3
        else:
            try:
                #decode save code
                #check hash
                clientHash=saveCode[:10]
                saveCode=saveCode[10:]
                
                # convert save code to binary
                saveBin = bin(int(saveCode, 16))[2:].zfill(len(saveCode) * 4)
                # print(saveBin)

                serverHash=sha256(saveBin.encode('ascii')+SERVER_SECRET.encode('ascii')).hexdigest()[:10]

                
                if clientHash != serverHash:
                    print("Invalid save code")
                    self.validGameState = False
                    return
                
                print("save code is valid")
                
                #get name from the first 80 bits
                n=int(saveBin[:80], 2)
                self.playerName = str(binascii.unhexlify('%x' % n))[2:-1]
                print("name:"+self.playerName)

                #get level from the next 4 bits
                self.playerLevel = int(saveBin[80:84], 2)
                print("level:"+str(self.playerLevel))

                #get health from the next 10 bits
                self.playerHealth = int(saveBin[84:94], 2)
                print("health:"+str(self.playerHealth))

                #get location from the next 7 bits
                self.currentLocationID = int(saveBin[94:101], 2)
                print("location:"+str(self.currentLocationID))

                #get health potion count from the next 3 bits
                self.healthPotionCount = int(saveBin[101:104], 2)
                print("health potion count:"+str(self.healthPotionCount))

                self.validGameState = True
                return
            except:
                self.validGameState = False
                return


    # print a hex encoded string that can be used to recreate the game state and all of its variables
    def printSaveCode(self):
        print("your save code is:")
        name = '{0:080b}'.format(int(binascii.hexlify(self.playerName.encode('utf-8')), 16))
        lvl = '{0:04b}'.format(self.playerLevel)
        hp = '{0:010b}'.format(self.playerHealth)
        locID = '{0:07b}'.format(self.currentLocationID)
        potionCount = '{0:03b}'.format(self.healthPotionCount)

        bStr = name+lvl+hp+locID+potionCount

        # print(bStr)

        hash=sha256(bStr.encode('ascii')+SERVER_SECRET.encode('ascii')).hexdigest()
        
        #get first 10 characters of hash
        hash = hash[:10]

        saveCode = '%0*X' % ((len(bStr) + 3) // 4, int(bStr, 2)) #https://stackoverflow.com/questions/2072351/python-conversion-from-binary-string-to-hexadecimal

        saveCode=hash+saveCode

        print(saveCode) 

    def levelUp(self):
        self.playerLevel += 1
        print("You have leveled up to level "+str(self.playerLevel)+"!")
        if self.playerLevel == 3:
            print("You find an intricate shield on the ground.")
            print("Its design and pattern matches that of your sword.")
            print("You pick it up and equip it.")
        if self.playerLevel == 6:
            print("You find a large metal device with the same design patterns as your sword and shield.\n It clicks into place as you attach it to your shield.")
            print("After closer inspection, it looks like the device can be connected to the tip of your sword, allowing you to swing your shield like a heavy axe.")
        if self.playerLevel == 10:
            print("You find a pair of strange batteries. Slotting them into your sword causes it to glow faintly.")
            print("Testing your sword on the fresh carcase, you feel a power building within the batteries.")
            print("As you stand over the corpse with your sword glowing a bright red, you wonder how much damage your axe will do when fully charged.\n")
       

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
            self.playerLevel = 1 # max 128 2^7
            self.playerHealth = 100 # max 1024 2^10
            self.currentLocationID = 0 # max 128 2^7
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

                #get level from the next 7 bits
                self.playerLevel = int(saveBin[80:87], 2)
                print("level:"+str(self.playerLevel))

                #get health from the next 10 bits
                self.playerHealth = int(saveBin[87:97], 2)
                print("health:"+str(self.playerHealth))

                #get location from the next 7 bits
                self.currentLocationID = int(saveBin[97:104], 2)
                print("location:"+str(self.currentLocationID))

                self.validGameState = True
                return
            except:
                self.validGameState = False
                return


    # print a hex encoded string that can be used to recreate the game state and all of its variables
    def printSaveCode(self):
        print("your save code is:")
        name = '{0:080b}'.format(int(binascii.hexlify(self.playerName.encode('utf-8')), 16))
        lvl = '{0:07b}'.format(self.playerLevel)
        hp = '{0:010b}'.format(self.playerHealth)
        locID = '{0:07b}'.format(self.currentLocationID)

        bStr = name+lvl+hp+locID

        # print(bStr)

        hash=sha256(bStr.encode('ascii')+SERVER_SECRET.encode('ascii')).hexdigest()
        
        #get first 10 characters of hash
        hash = hash[:10]

        saveCode = '%0*X' % ((len(bStr) + 3) // 4, int(bStr, 2)) #https://stackoverflow.com/questions/2072351/python-conversion-from-binary-string-to-hexadecimal

        saveCode=hash+saveCode

        print(saveCode) 

        
       

'''
World Cup Draw Generator by Kotori Minalinsky Ancestor
Do NOT change the following code.
'''

class Team:
    
    def __init__(self, name, abbr, seed=1, host=False):
        self.__name = name.title()
        self.__abbr = abbr.upper()
        while True:
            try:
                self.__seed = int(seed)
                break
            except:
                print('Current Seed Parameter is: {}'.format(self.getSeed()))
                seed = input('Invalid Seed Parameter Entered.\nPlease enter an Integer. (Default: 1) ')
                if seed == '' or seed.isspace():
                    seed = 1
                continue
            
        self.__host = host
    
    def __repr__(self):
        return 'Team Name: {}\nTeam Abbreviation: {}\nSeed Parameter: {}\nTeam is Host: {}'.format(self.__name, self.__abbr, self.__seed, self.__host)
    
    def __str__(self):
        return '{} ({})'.format(self.__name, self.__abbr)
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name.title()
    
    def getAbbr(self):
        return self.__abbr
    
    def setAbbr(self, abbr):
        self.__abbr = abbr.upper()
    
    def getSeed(self):
        return self.__seed
    
    def setSeed(self, seed):
        while True:
            try:
                self.__seed = int(seed)
                break
            except:
                print('Current Seed Parameter is: {}'.format(self.getSeed()))
                seed = input('Invalid Seed Parameter Entered.\nPlease enter an Integer. (Default: 1) ')
                if seed == '' or seed.isspace():
                    seed = 1
                continue
    
    def checkIfHost(self):
        return self.__host
    
    def makeHost(self):
        self.__host = True
    
    def unmakeHost(self):
        self.__host = False

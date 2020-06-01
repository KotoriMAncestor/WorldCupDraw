'''
World Cup Draw Generator by Kotori Minalinsky Ancestor
Do NOT change the following code.
'''

class Group:
    
    def __init__(self, name, count=0):
        if type(name) == int:
            name = chr(name+65)
        self.__name = name
        self.__seeds = ['NA'] * count
        
    def __repr__(self):
        seedStr = [str(team) for team in self.__seeds]
        return 'Group Name: {}\nNumber of Team in Group: {}\nTeams in Group:\n'.format(self.__name, str(self.getNumberOfTeams())) + '\n'.join(seedStr)
    
    def __str__(self):
        seedStr = [str(team) for team in self.__seeds]
        return 'Group {}: \n'.format(self.__name) + '\n'.join(seedStr)
    
    def addToGroup(self, team):
        seed = team.getSeed()
        try:
            if self.__seeds[seed-1] == 'NA':
                self.__seeds.pop(seed-1)
        except:
            pass
        finally:
            self.__seeds.insert(seed-1, team)
            
    def addToGroupPos(self, team, pos):
        try:
            if self.__seeds[pos-1] == 'NA':
                self.__seeds.pop(pos-1)
        except:
            pass
        finally:
            self.__seeds.insert(pos-1, team)
    
    def removeFromGroup(self, seed=None):
        if self.__seeds == []:
            print('No team to delete.')
            return 
        if seed == None:
            print('Please select team to delete (1~{})'.format(len(self.__seeds)))
            for i in range(len(self.__seeds)):
                print('{} ({})'.format(self.__seeds[i], str(i+1)))
            while True:
                try:
                    seed = int(input('Your choice is: '))
                    if seed < 1 or seed > len(self.__seeds):
                        raise ValueError
                    print('Team {} will be deleted.'.format(self.__seeds[seed-1].getName()))
                    x = input('Confirm? (Y/n) ')
                    if x.lower() == 'n':
                        continue
                    break
                except:
                    print('Invalid number.\nPlease try again!')
                    continue
        self.__seeds[seed-1] = 'NA'
    
    def getNumberOfTeams(self):
        return len(self.__seeds)
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if type(name) == int:
            name = chr(name+65)
        self.__name = name
    
    def addTeam(self, count):
        if count > 0:
            self.__seeds += ['NA'] * count
    
    def deleteTeam(self, count):
        if count > 0:
            self.__seeds = self.__seeds[:-1*count]
    
    def popTeam(self, index):
        if index >= 0 and index < len(self.__seeds):
            return self.__seeds.pop(index)
        else:
            return None
    
    def getTeamFromIndex(self, index):
        return self.__seeds[index]
    
    def getTeamFromSeed(self, seed):
        return self.__seeds[seed-1]
    
    def getGroupAsList(self):
        return self.__seeds
    
    def appendGroup(self, g):
        self.__seeds += g.getGroupAsList()
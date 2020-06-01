'''
World Cup Draw Generator by Kotori Minalinsky Ancestor
Do NOT change the following code.
'''


from draw_functions import *
from time import sleep

print('Welcome to Draw Generator!\nNow loading teams from teams.txt')
sleep(1)
pool = importTeamsFromFile()
try:
    number_of_teams = pool.getNumberOfTeams()
except:
    sleep(3)
    exit()
pool = groupTeams(pool)

print()
displayPool(pool)

print()
print('There are {} Teams loaded.'.format(str(number_of_teams)))
print()

sleep(3)
count, team_per_group = getNumOfGroup(number_of_teams)

groups = emptyGroups(count, team_per_group, number_of_teams)

drawHosts(pool, groups)

sleep(1)
print('The hosts are drawn.')
print()

displayGroups(groups)

drawTeams(pool, groups)

sleep(3)
print('The final draw result is shown below.')
print()
displayGroups(groups)
print()
sleep(3)

writeGroupsToFile(groups)

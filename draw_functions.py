'''
World Cup Draw Generator by Kotori Minalinsky Ancestor
Do NOT change the following code.
'''

from team import Team
from group import Group
from time import sleep
from random import randrange as choose_number

def importTeamsFromFile(filename='teams.txt'):
    try:
        file = open(filename, 'r', encoding='utf-8')
        list_of_teams = file.read().splitlines()
        pool = Group('of Teams to be drawn')
        for team_line in list_of_teams:
            if team_line == '' or team_line.isspace() or team_line[0] == '#':
                list_of_teams.remove(team_line)
            else:
                team_details = [t.strip() for t in team_line.split(',')]
                team = Team(*team_details)
                pool.addToGroup(team)
        file.close()
        return pool
            
    except FileNotFoundError:
        print('Cannot read file from provided file path')
        return []
    
    except:
        print('Error reading file')
        return []

def groupTeams(teams):
    group_of_teams = {}
    for team in teams.getGroupAsList():
        seed = team.getSeed()
        if seed not in group_of_teams:
            group_of_teams[seed] = Group('Seed ' + str(seed))
        group_of_teams[seed].addToGroup(team)
    return group_of_teams
    
def getNumOfGroup(number_of_teams):
    while True:
        try:
            count = int(input('How many groups do you want to have? '))
            if count <= 0 or count > number_of_teams:
                raise ValueError
            break
        except:
            print('Value Invalid! Please enter an Integer.')
            continue
    team_per_group = (number_of_teams + count - 1) // count
    print()
    return count, team_per_group

def emptyGroups(count, team_per_group, number_of_teams):
    excess = number_of_teams - count * (team_per_group - 1)
    empty_groups = []
    for i in range(count):
        if excess > 0:
            empty_groups.append(Group(i, team_per_group))
        else:
            empty_groups.append(Group(i, team_per_group-1))
        excess -= 1
    return empty_groups

def displayGroups(groups, num=None):
    if num == None:
        for g in groups:
            print(g)
            print()
    else:
        print(groups[num])

def displayPool(pool):
    for seed in pool.values():
        print(seed)
        print()

def drawHosts(pool, groups):
    list_of_hosts = []
    for seed in pool.values():
        i = 0
        while i < seed.getNumberOfTeams():
            team = seed.getTeamFromIndex(i)
            if team.checkIfHost():
                list_of_hosts.append(seed.popTeam(i))
            else:
                i += 1
    for j in range(len(list_of_hosts)):
        groups[j].addToGroup(list_of_hosts[j])

def drawTeams(pool, groups):
    for seed, teams in pool.items():
        for g in groups:
            if seed > g.getNumberOfTeams():
                pass
            elif g.getTeamFromSeed(seed) == 'NA':
                try:
                    if teams.getNumberOfTeams() == 0:
                        raise IndexError
                    print('Now drawing Seed {} of Group {}'.format(seed, g.getName()))
                    sleep(3)
                    tmp = choose_number(teams.getNumberOfTeams())
                    team = teams.popTeam(tmp)
                    g.addToGroup(team)
                    
                    print()
                    print('Team {} goes into Group {}.\n'.format(team, g.getName()))
                    sleep(1)
                    print(g)
                    print()
                except:
                    pass
    drawRemainingTeams(pool, groups)

def drawRemainingTeams(pool, groups):
    remaining_teams = Group('Teams')
    for teams in pool.values():
        remaining_teams.appendGroup(teams)
    for seed in range(1, groups[0].getNumberOfTeams()+1):
        for g in groups:
            if seed > g.getNumberOfTeams():
                pass
            elif g.getTeamFromSeed(seed) == 'NA':
                try:
                    if remaining_teams.getNumberOfTeams() == 0:
                        raise IndexError
                    print('Now drawing Seed {} of Group {}'.format(seed, g.getName()))
                    sleep(3)
                    tmp = choose_number(remaining_teams.getNumberOfTeams())
                    team = remaining_teams.popTeam(tmp)
                    g.addToGroupPos(team, seed)
                    
                    print()
                    print('Team {} goes into Group {}.\n'.format(team, g.getName()))
                    sleep(1)
                    print(g)
                    print()
                except:
                    pass

def writeGroupsToFile(groups, filename='output.txt'):
    while True:
        try:
            output_prompt = input('Do you want to save this draw result? [Y/n]')
            if output_prompt.lower() != 'y' and output_prompt.lower() != 'n':
                raise ValueError
            if output_prompt.lower() == 'y':
                print('The output file will be saved as output.txt\n')
                sleep(1)
                file = open(filename, 'w', encoding='utf-8')
                for g in groups:
                    file.write(str(g)+'\n\n')
                file.close()
            print('Thank you for using Draw Generator!\nThis program will close in 5 seconds.')
            sleep(5)
            break
        except:
            continue

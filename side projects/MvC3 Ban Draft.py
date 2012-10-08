import random

ROSTER = ['Akuma', 'Amaterasu', 'Arthur', 'C.Viper', 'Chris', 'Chun Li', 'Dante'
          , 'Felicia', 'Haggar', 'Hsien Ko', 'Jill', 'Morrigan', 'Ryu', 'Spencer'
          , 'Trish', 'Tron Bonne', 'Viewtiful Joe', 'Wesker', 'Zero', 
          'Captain America', 'Deadpool', 'Dormammu', 'Dr.Doom', 'Hulk', 'Iron Man', 
          'Magneto', 'MODOK', 'Phoenix', 'Sentinel', 'She Hulk', 'Spider-Man', 
          'Shuma Gorath', 'Storm', 'Super-Skrull', 'Taskmaster', 'Thor', 
          'Wolverine', 'X-23']
ROSTER_NODLC = ['Akuma', 'Amaterasu', 'Arthur', 'C.Viper', 'Chris', 'Chun Li', 'Dante'
          , 'Felicia', 'Haggar', 'Hsien Ko', 'Morrigan', 'Ryu', 'Spencer'
          , 'Trish', 'Tron Bonne', 'Viewtiful Joe', 'Wesker', 'Zero', 
          'Captain America', 'Deadpool', 'Dormammu', 'Dr.Doom', 'Hulk', 'Iron Man', 
          'Magneto', 'MODOK', 'Phoenix', 'Sentinel', 'She Hulk', 'Spider-Man', 
          'Storm', 'Super-Skrull', 'Taskmaster', 'Thor', 'Wolverine', 'X-23']

def random_batch(roster, players):
    """Return a random batch of characters from roster depending on the number
    of players playing."""
    
    amount = (players * 3) + players
    batch = []
    while len(batch) < amount:
        index = random.randrange(0, len(roster))
        batch.append(roster[index])
        roster.pop(index)
    return batch

if __name__ == "__main__": 
    print "Made by Kocha"
    print "~~~~~~~~~~~~~~~~~~~~~"
    print "This is a simple scipt used to faciliate a ban draft mode similar"
    print "to the one seen in MOBA games such as DOTA. Just input the information" 
    print "asked and everything will be made easy! Let's get started."
    print '========================================'
    print '========================================'
    DLC = raw_input("Are you playing with DLC characters?(input y or n):  ")
    while DLC != 'y' and DLC != 'n':
        DLC = raw_input("Wrong input, only y for yes or n for no. Are you playing with DLC characters?:   ")
    if DLC == 'y':
        roster = ROSTER
    else:
        roster = ROSTER_NODLC
    players = raw_input("How many players are playing?(input digit from 2-6):  ")
    try :
        x = int(players)
        while x < 2 or x > 6:
            players = raw_input("Try again, only 2-6 players will work. How many players are playing?:   ")
    except:
        players = raw_input("Try again, only 2-6 players will work. How many players are playing?:   ")
    draft = random_batch(roster, x)
    print '========================================'
    print "This is the draft batch, each player may ban one character"
    print '========================================'
    for item in draft:
        print item
    print '========================================'
    for i in xrange(x):
        ban = raw_input("Please type one character's name to ban, exactly as it is from above:   ")
        while ban not in draft:
            ban = raw_input("Couldn't find that name in roster, try again:   ")
        draft.remove(ban)
        print '========================================'
        for item in draft:
            print item
        print '========================================'
    print "The picking begins! Please keep track of your own team so far"
    print '========================================'
    for i in xrange(len(draft)):
        pick = raw_input("Pick one character from roster:   ")
        while pick not in draft:
            pick = raw_input("Couldn't find that name, please type exactly as in roster:   ")
        draft.remove(pick)
        print '========================================'
        for item in draft:
            print item
        print '========================================'
    
    print "That's it, have fun!"
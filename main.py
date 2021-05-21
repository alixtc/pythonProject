import re
a = 'Rilke'
b = 'martin'

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        name = name + " plays banjo" 
    else:
        name = name + " does not play banjo"
    return name

are_you_playing_banjo(a)
are_you_playing_banjo(b)
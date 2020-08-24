# Function to Calculate XP Gain from Battle
def xp_gain(ev_yield, level, level_opponent):
    return (((1 * ev_yield * level_opponent) / (5 * 1) * (((2 * level_opponent + 10) ** 2.5) / ((level_opponent + level + 10) ** 2.5) + 1)) * 1 * 1 * 1)

# Functions to determine amount of XP a Pokemon has based on appropriate XP Formula
def xp_medium_slow(level):
    return (6/5 * level ** 3) - (15 * level ** 2) + (100 * level) - 140

def xp_fast(level):
    return ((4*level**3) / 5)

def xp_medium_fast(level):
    return (level**3)

def xp_slow(level):
    return ((5*level**3)/4)

# Functions to determine the level based on Current XP
def get_level_medium_slow(xp):
    return (((5*(81*xp**2-16695*xp+1387600)**.5)/108)
    +(((((5*xp+700)/2)-(3125/3))/6)+(15625/216)))**(1/3)-(125/(12*(((5*(81*xp**2-16695*xp+1387600)**.5)/108)
    +((((5*xp+700)/2)-(3125/3))/6)+(15625/216))**(1/3)))+(25/6)

def get_effort_value_from_xp(xp):
    return ((xp**.5)/4)

def get_xp_from_effort_value(effort_value):
    return (16*(effort_value)**2)

# Debug Statements
print("Slow XP: {slow_xp}".format(slow_xp=xp_slow(100)))
print("Medium Slow XP: {medium_slow_xp}".format(medium_slow_xp=xp_medium_slow(46)))
print(int(get_level_medium_slow(91241)+.00001))
print("Fast XP: {fast_xp}".format(fast_xp=xp_fast(100)))
print("Medium Fast XP: {medium_fast_xp}".format(medium_fast_xp=xp_medium_fast(100)))
print("Experience for Rayquaza with 231 EV is {experience}".format(experience=get_xp_from_effort_value(231)))
print("EV for Meganium with 91,241 xp is {effort_value}".format(effort_value=get_effort_value_from_xp(91241)))
#print(xp_gain(3, 1, 10))



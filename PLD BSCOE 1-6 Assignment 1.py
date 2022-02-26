"""
This will print full name similar to an introduction
and also spell the name using loops.
"""
def header():
    """Print a header design with what the program is about"""
    title = "**PRINT NAME/INTRODUCTION**"
    flower = "*" * len(title) 
    print('\033[33m{} \n{} \n{}\033[00m'.format(flower, title, flower)) #another version of printing a variable through output formatting

def spellName():
    """Spell name one character per line"""
    name = fullName.split(" ") #This will turn the string into a list which the whitespace will serve as a separator
    rep = 0 # initialization
    while rep<= 3:
        for cha in name[rep]: #loop inside a loop for every element of the list
            print("\033[36m %s \033[00m" % (cha)) # older version of printing a variable before string formats was introduced
        rep+=1

fullName = "Mary Gwen G. Susa"
header()
print("\033[32mHello! ^_^\033[00m I am \033[04m\033[95m{}\033[00m".format(fullName)) 
spellName()


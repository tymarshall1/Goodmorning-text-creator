import random

#first part of morning text
mornings = [
'Good morning baby!', 
'Good morning booski!', 
'Good morning princess!',
'Morning babe'
]
#second part of morning text
mornings1 = [
'I hope you are having a wonderfull day today.', 
'I miss you so much!',
'I cant wait to see you later!',
'I hope you had a great night sleep.'
]
#third part of the morning text
mornings3 = [
'I love you more than anything',
'I love you to the moon and back',
'I love you so much!',
'You are the best thing that has ever happened to me',
'You are a beautiful person inside and out',
'We fit together like puzzle pieces',
'You comeplete me'
]
#emoji list
emojis = [
"\U0001F49C",
"\U0001F499",
"\U0001F49A",
"\U0001F49B",
"\U0001F9E1",
"\u2764\ufe0f",
"\U0001F48B",
"\U0001F496",
"\U0001F60D",
"\U0001F618",
]
emojis1 = [
"\U0001F49C",
"\U0001F499",
"\U0001F49A",
"\U0001F49B",
"\U0001F9E1",
"\u2764\ufe0f",
"\U0001F48B",
"\U0001F496",
"\U0001F60D",
"\U0001F618",
]
emojis2 = [
"\U0001F49C",
"\U0001F499",
"\U0001F49A",
"\U0001F49B",
"\U0001F9E1",
"\u2764\ufe0f",
"\U0001F48B",
"\U0001F496",
"\U0001F60D",
"\U0001F618",
]
#grabs and randomizes the first phrase of text    ##change randint range if add more phrases
def start():
    get_num = random.randint(0,3)
    for index,phrase in enumerate(mornings):
        if index == 0 and index == get_num:
            return phrase
        elif index == 1 and index == get_num:
            return phrase
        elif index == 2 and index == get_num:
            return phrase
        elif index == 3 and index == get_num:  
            return phrase

#grabs and randomizes the seceond phrase of the text ##make sure to change randint if add more phrases
def middle():
    get_num = random.randint(0,3)
    for index,phrase in enumerate(mornings1):
        if index == 0 and index == get_num:
            return phrase
        elif index == 1 and index == get_num:
            return phrase
        elif index == 2 and index == get_num: 
            return phrase
        elif index == 3 and index == get_num:
            return phrase

#grabs and randomizes third phrase
def middle2():
    get_num = random.randint(0,6)
    for index,phrase in enumerate(mornings3):
        if index == 0 and index == get_num:
            return phrase
        elif index == 1 and index == get_num:           
            return phrase
        elif index == 2 and index == get_num:            
            return phrase
        elif index == 3 and index == get_num:
            return phrase
        elif index == 4 and index == get_num:            
            return phrase
        elif index == 5 and index == get_num:            
            return phrase
        elif index == 6 and index == get_num:
            return phrase

#grabs emojis from emoji lists
def emoji():
    get_num = random.randint(0,9)
    for index,phrase in enumerate(emojis):
        if index == 0 and index == get_num:
            return phrase
        elif index == 1 and index == get_num:           
            return phrase
        elif index == 2 and index == get_num:            
            return phrase
        elif index == 3 and index == get_num:
            return phrase
        elif index == 4 and index == get_num:            
            return phrase
        elif index == 5 and index == get_num:            
            return phrase
        elif index == 6 and index == get_num:
            return phrase
        elif index == 7 and index == get_num:            
            return phrase
        elif index == 8 and index == get_num:            
            return phrase
        elif index == 9 and index == get_num:
            return phrase

def emoji1():
    get_num = random.randint(0,9)
    for index,phrase in enumerate(emojis1):
        if index == 0 and index == get_num:
            return phrase
        elif index == 1 and index == get_num:           
            return phrase
        elif index == 2 and index == get_num:            
            return phrase
        elif index == 3 and index == get_num:
            return phrase
        elif index == 4 and index == get_num:            
            return phrase
        elif index == 5 and index == get_num:            
            return phrase
        elif index == 6 and index == get_num:
            return phrase
        elif index == 7 and index == get_num:            
            return phrase
        elif index == 8 and index == get_num:            
            return phrase
        elif index == 9 and index == get_num:
            return phrase

def emoji2():
    get_num = random.randint(0,9)
    for index,phrase in enumerate(emojis2):
        if index == 0 and index == get_num:
            return phrase
        elif index == 1 and index == get_num:           
            return phrase
        elif index == 2 and index == get_num:            
            return phrase
        elif index == 3 and index == get_num:
            return phrase
        elif index == 4 and index == get_num:            
            return phrase
        elif index == 5 and index == get_num:            
            return phrase
        elif index == 6 and index == get_num:
            return phrase
        elif index == 7 and index == get_num:            
            return phrase
        elif index == 8 and index == get_num:            
            return phrase
        elif index == 9 and index == get_num:
            return phrase





beginning = start()
middle_text = middle()
middle_text_1 = middle2()
emo = emoji()
emo1 = emoji1()
emo2 = emoji2()
print(f'{beginning} {emo} {emo1} {middle_text} {emo2} {middle_text_1} {emo} xoxoxoxoxoxo')


#for x,y in enumerate(mornings1):
    #print(x,y)
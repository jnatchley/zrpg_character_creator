import random
import sys
import time
from occupation import job

##This makes text appear slowly
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

##Beginning dictionary to store character's info
my_character = {'character_name': '', 'character_age': 0, 'character_race': '', 'character_occupation': 'nothing'}

print("""
@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@/&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@/@/.%%&@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@(/(/#%.%#&%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@&@@@@@.(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@********** (&***********@@@@*@@*@*@**@@@*@@*@%*@*@**@*@*@*@*@@***@*@@@@@@@@@@
@@****@@@@@@(((((@@******&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@*@@@@@@@@@@(((@***@***@@@***********%@******%@@@@*********@@@@@@@*****@@@@@@@@
@@@@@@@@@@@@@&(***@@**@@@@@@****@@@@***@@*****@@@@@@*****@@****@@@@/*****@@@@@@@
@@@@@@@@@@@@@&**/@**@@@@@@@@****@@@%@**@@*****@@@@@@****/@@@****@@@*******@@@@@@
@@@@@@@@@@@@*******@@@@@@@@@********@@@@@*****@@@@@@*****@@@****@@***@****@@@@@@
@@@@@@@@@@*******@@****#@@@@****@@**@@@@@*****@@@&@@*****@@@****@/***/@****@@@@@
@@@@@@@@@**@@**(/@@@@*@@@*&@****@@@@@**@@*****@@&*@@****@@@/****@**/@@@****&@@@@
@@@@@@@**@@***%(@@@@@*@@@@@@****@@@@*/&@@****/@@**@@*****@*****@***@@@@*****@@@@
@@@@@***@***@&&@@@@@&@@@@@**********************&*@*********@@*****/@@@*****#*@@
@@@@******@@@&&&@@@*@@@****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@***********&@&@********@@@@*@@*@(**@@**@@@@*@@*@@****@*/@@@@@**@*#*@@*@@*@@*@*
@@@@@@@@@@@@@&&&@@@@@@@@@@@@@*@@**@@@@@@@@@@@@@@@@@@@@@@@*@*@*@@*@@*@@@@@@@@@@@@
@@@@@@@@@@@@@&&(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@ ((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@ &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

## introduction
def welcome_message():
    print_slow("Welcome to the ZRPG character creator! We are going to answer some questions to create a randomized character for your zrpg needs.")
    print()
welcome_message()

## Character's name
class Char_name:
    print_slow("Name your character something fun:  ")
    my_name = input()
    print()
    print_slow(f"Okay, if you're sure about that... Your character's name will be {my_name}.")
    print()

name = Char_name.my_name

my_character['character_name'] = name


## Decide the age of the character, this is done by counting the number of letters that the user inputs while they explain their likes and dislikes.
class Char_age:
    print_slow("Now tell me a bit about yourself. Don't be shy! Tell me some things you like, and some things you dislike.  ")
    my_age = len(input())

    if my_age <= 20:
        print_slow(f"You don't speak much, do you? Like a child. So lets make your character {my_age} years old. A youngling. ")
    elif 21 <= my_age < 40:
        print_slow(f"Good long answer. That's the kind of talk I'd see from someone with some maturity. Let's make your character {my_age} years old.")
    else: 
        print_slow(f"Whoa, you sure are a talker. Maybe you should learn to be a bit more brief... since you can't shut up, let's make your character a bit older. Let's make your character {my_age} years old.")

age = Char_age.my_age

my_character['character_age'] = age

print()

## Deciding the race of the character, which is done by providing a list of words and the word they choose will decide their character's race. In the future this may be changed into a switch
class Char_race:
    print_slow("Okay, now we will choose the race of your character. What will you be? A strong sturdy goron? A graceful zora? Let's find out! ")
    print_slow("Here is a list of adjectives. Please type the number of the adjective you like! \n 1. goofy \n 2. noble \n 3. mighty \n 4. imposing \n 5. dedicated \n 6. plain \n 7. mischievous \n 8. shifty \n 9. dangerous \n 10. regal \n 11. agile \n 12. powerful \n 13. refined: \n What do you choose?  ")
    my_race = input()
    if my_race == "1":
        my_race = "Bokoblin"
        print_slow("Goofy huh? What's more goofy than a Bokoblin? Congrats on your piggy little friend!")
    elif my_race == "2":
        my_race = "Darknut"
        print_slow("Going for the tall dark and handsome type? A Darknut is for you!")
    elif my_race == "3":
        my_race = "Gerudo"
        print_slow("Strong and mighty, the gerudo are the race for you. These strong ladies are lean mean fighting machines.")
    elif my_race == "4":
        my_race = "Goron"
        print_slow("Massive, looming, but with a heart of gold, your character is a goron!")
    elif my_race == "5":
        my_race = "Guardian Fairy"
        print_slow("Who else is dedicated to their followers like a guardian fairy?")
    elif my_race == "6":
        my_race = "Hylian"
        print_slow("Plain? Well unless you are our Hero of Time, you're going to be basic. Hylian it is!")
    elif my_race == "7":
        my_race = "Korok"
        print_slow("Yahaha! Korok it is!")
    elif my_race == "8":
        my_race = "Lizalfos"
        print_slow("Shifty buggers, those lizalfos are. Big camouflage points though, and you can climb walls. Fun!")
    elif my_race == "9":
        my_race = "Moblin"
        print_slow("They may be a little dumb, but Moblins are as dangerous as you're going to get!")
    elif my_race == "10":
        my_race = "Rito"
        print_slow("BIRDOS! Sorry, I was excited. Ritos are my favorite, and now you get to make a fluffy bird character!")
    elif my_race == "11":
        my_race = "Sheikah"
        print_slow("Our creative and agile ninjas, the Sheikah! There are two branches, the kakariko village sheikah or the yiga clan!")
    elif my_race == "12":
        my_race = "Wizzrobe"
        print_slow("A unique choice, the wizzrobes are! They may look a big creepy, but they can be quite powerful and have a lot of magic you can play with!")
    elif my_race == "13":
        my_race = "Zora"
        print_slow("Refined, elegant, and poise... unless you go the route of a cute dumbo like Prince Sidon. You've got Zora!")
    else:
        my_race = "Bokoblin"
        print_slow("Uh oh, that's not one of the options... Uhhh since it seems you're not very... intellectually talented... let's just make your character a Bokoblin.")

race = Char_race.my_race

my_character['character_race'] = race

print()

## Here we will be deciding the occupation of the character. First we pull the current occupation from the dictionary, then randomly choose an occupation from a list
print_slow(f"Now let's see what occupation your character has. Let's see, currently {name}'s occupation is: ")
##Code below pulls out the purposefully place "nothing" in the dictionary before changing it
print_slow([value for value in my_character.values()][3])
print()
print_slow("Yikes. Uh, we better change that. We can't have your character being a bum on the street. ")
print()
print_slow(f"How about we choose something fun... something exciting... something that you can be creative with! Okay, I'm going to grab something random. Let's see... you shall be a/an {job}!")
print()
my_character['character_occupation'] = job

## Here we will show the user all of the data of their character
def speak():
    print_slow("Phew, that took some work but we finally have a good base for your character! Let's see the data we've collected: ")
    print()
speak()

print()

for key, value in my_character.items():
    print(key, value)
print()
print_slow("Oh ew, that doesn't look very neat, does it. Sorry. I'm just learning how to code. Let's clean that up a bit.")
print()
print_slow(f"Your character's name is {name}. Your character's age is {age}. Your character's race is {race}, and finally, your character's occupation is {job}.")
print()

def ending_message(your_name):
    print_slow("Thank you for trying out this program, " + your_name + "! I hope you had fun, and be sure to check out zrpg.net if this has inspired you to bring your character to life! See you there! ")
print_slow("Now, what is YOUR name?  ")
ending_message(input())

print()

## The function below is a bit redundant, but used to learn how 'return' is used

def goodbye(final, final2):
    result = final + final2
    return result
print(goodbye('Good', 'bye!'))

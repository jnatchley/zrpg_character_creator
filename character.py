##import random for occupation?
##Make sure to import occupation file

my_character = {'character_name': '', 'character_age': 0, 'character_race': '', 'character_occupation': 'nothing'}

##introduction

print("Welcome to the ZRPG character creator! We are going to answer some questions to create a randomized character for your zrpg needs.")


##Character's name
name = input("Name your character something fun:  ")
print(f"Okay, if you're sure about that... Your character's name will be {name}.")

my_character['character_name'] = name


## Decide the age of the character, this is done by counting the number of letters that the user inputs while they explain their likes and dislikes.
age = len(input("Now tell me a bit about yourself. Don't be shy! Tell me at least three things you like, and some things you dislike.  "))

if age <= 20:
    print(f"You don't speak much, do you? Like a child. So lets make your character {age} years old. A youngling. ")
elif 21 <= age < 40:
    print(f"Good long answer. That's the kind of talk I'd see from someone with some maturity. Let's make your character {age} years old.")
else: 
    print(f"Whoa, you sure are a talker. Maybe you should learn to be a bit more brief... since you can't shut up, let's make your character a bit older. Let's make your character {age} years old.")

my_character['character_age'] = age


## Deciding the race of the character, which is done by providing a list of words and the word they choose will decide their character's race
race = "placeholder"


## Here we will be deciding the occupation of the character. First we pull the current occupation from the dictionary, then randomly choose an occupation from a list
print(f"Now let's see what occupation your character has. Let's see, currently {name}'s occupation is: ")

print([value for value in my_character.values()][3])

print("Yikes. Uh, we better change that. We can't have your character being a bum on the street. ")
occupation = "placeholder"


##Here we will show the user all of the data of their character
print("Phew, that took some work but we finally have a good base for your character! Let's see the data we've collected: ")
for key, value in my_character.items():
    print(key, value)
print("Oh ew, that doesn't look very neat, does it. Let's clean that up a bit.")
print(f"Your character's name is {name}. Your character's age is {age}. Your character's race is {race}, and finally, your character's occupation is {occupation}.")
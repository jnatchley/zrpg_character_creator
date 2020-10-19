##

my_character = {'name': '', 'age': 0, 'race': '', 'occupation': ''}

print("Welcome to the ZRPG character creator! We are going to answer some questions to create a randomized character for your zrpg needs.")

name = input("Name your character something fun:  ")
print("Okay, if you're sure about that... Your character's name will be {}.".format(name))

age = len(input("Okay, now tell me a bit about yourself. Don't be shy! Tell me at least three things you like, and some things you dislike.  "))

if age <= 20:
    print("You don't speak much, do you? Like a child. So lets make your character {} years old. A youngling. ".format(age))
elif 21 <= age < 40:
    print("Good long answer. That's the kind of talk I'd see from someone with some maturity. Let's make your character {} years old.".format(age))
else: 
    print("Whoa, you sure are a talker. Maybe you should learn to be a bit more brief... since you can't shut up, let's make your character a bit older. Let's make your character {} years old.".format(age))
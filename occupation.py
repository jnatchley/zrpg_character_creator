import random

## occupation lists - commented out so can pull from text file instead. However, code below works. 
#occupation_list = ['cook', 'soldier', 'healer', 'student', 'fisherman', 'teacher', 'cartographer', 'reporter', 'researcher', 'explorer', 'professor', 'knight', 'scout', 'actor', 'bard', 'poet', 'writer', 'scientist', 'miller', 'weaver', 'spinner', 'fur trader', 'butcher', 'brewer', 'snakeoil salesperson', 'pickpocket', 'fortune teller', 'tinker', 'smith', 'leatherworker', 'librarian', 'rancher', 'scribe', 'traveling storyteller', 'woodsman', 'fletcher',
#'tailor', 'composer', 'beekeeper', 'Sage', 'Salt seller', 'Miner', 'chimney sweep', 'Midwife', 'Maid', 'Butler', 'Sommelier', 'Baker', 'Caterer', 'courier', 'Jeweler']

occupation_list = [line.strip() for line in open('jobs.txt')]

job = random.choice(occupation_list)
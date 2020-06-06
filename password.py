#Password Generator
import random, string

print('Password Generator')

#User Input
letter = int(input('Input the number of Letters you want for your Password: '))
number = int(input('Input the number of integers you want for your Password: '))
character = int(input('Input the number of Characters you want for your Password: '))

all_numbers =  ''.join(random.choice(string.digits) for i in range(number))
all_letters = ''.join(random.choice(string.ascii_letters) for i in range(letter))
all_characters = ''.join(random.choice(string.punctuation) for i in range(character))

formation = (all_numbers + all_letters + all_characters)
password_generator = random.sample(formation, len(formation)) 
password = ''.join((password_generator))
if len(formation) > 6:
    print('The password total should be a minimum of 6 characters, Try Again!')
else:
    print('Your password is {}'.format(password))
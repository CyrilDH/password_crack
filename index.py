
import secrets
import string
import random

# length = int(input('\nEnter the length of password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
# date = str(input('\nEnter the date: '))
name = str(input('\nEnter the name: '))
upper = []
lower = []

# surname = str(input('\nEnter the surname: '))
#
# def date() :
#     print(date)
# def name() :
#     print(name)
# def surname() :
#     print(surname)

def generate_password():
    for caractere in name:
       upper.append(caractere.upper())
       lower.append(caractere.lower())
       all = lower + upper
       indice = indice + 1
       print(upper[indice])
#        if(upper[indice] == lower[indice]):
#        upperRandom = random.sample(upper, len(upper))
#        all =  lower + upper
#        chaine = " ".join(sorted(set(all), key=all.index))

#     def randomUpper():
#     #         print(this.upper)
#     #         print(caractere.lower() , end='')
#     #  password = ''.join(secrets.choice(all) for i in range(len(name)))

generate_password()
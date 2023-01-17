import random
import string
def genrate_random_password(length):
    # choose from all lowercase letter
    while True:
        guess = string.ascii_lowercase
        password = ''.join(random.choice(guess) 
        for i in range(length))
        print("[scanning][+] \t", password,'\n')
        ''' put your password here 
        what is your password 
        in my case password is yum'''
        if password=='yum':
            print(f"your password is {password}")
            break
        else:
            print("please wait")
# Also set the length of a password
genrate_random_password(3)
# this video is for educational purpose only
# thanks..for watching...
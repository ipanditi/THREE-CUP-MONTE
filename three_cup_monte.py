from random import shuffle
mylist= ['','O','']

#function 1
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#function 2
def player_guess():
    
    
    guess = " "
    
    while guess not in ['0','1','2']:
        guess = input('pick a number: 0,1 or 2')
        
    return int(guess)

#function 3
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('Correct!')
    else:
        print('Wrong')
        print(mylist)

#ALGORITHM
# INITIAL LIST
mylist = ['', 'O','']

# SHUFFLE LIST
mixed_up_list = shuffle_list(mylist)

# USER GUESS 
guess= player_guess()

# CHECK GUESS
check_guess(mixed_up_list,guess)                

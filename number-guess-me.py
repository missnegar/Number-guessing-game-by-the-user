import random
true_number = random.randint(1,99)
print(true_number)

guessnumber = input("what is your number ? ")
guessnumber = int(guessnumber)

while guessnumber != true_number :    
    if guessnumber < true_number:    
        print( " My number is bigger than you!")
    else:    
        print("My number is smaller than you")
    guessnumber = input("Guess Another Number : ")
    guessnumber = int(guessnumber)
print("BAD ASS YOU RIGHT...!")
    
"""Odd or Even Project: Check whether the input from a user between 1 and 1000 is even or odd"""

# ask for user input 
user_input = int(input("What number are you thinking? : "))

    # check if number is less than 1 and is greater than 1000

while 0 < user_input <= 1000:
    # if input divided by 2 = 0 print number is even else odd
    if user_input / 2 == 0:
        print(f"That's an even number! {user_input} Have another?")            
    else:
        print(f"That's an odd number! {user_input} Have another?")  
    break


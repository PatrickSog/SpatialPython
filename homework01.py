########################################
# Author: Patrick Sogno
# Date: May, 2019
# Python version: 3.7
# Spyder version: 3.3.2
# e-mail: patrick.sogno@stud-mail.uni-wuerzburg.de
########################################
# Background: 
# This is python homework from university.
# It is therefore mostly for personal use,
# however, if you find something useful for
# your own project, help yourself :).
# I'm a python beginner but I will try to
# answer questions related to the code
# via e-mail.
########################################





###### Exercise 1: #-------------------------#
j = 9
j = j**(0.5)
print(j)


###### Exercise 2:
# Empty string:
print("")

# Write sth. with ', ", and \
print("'"), print('"'), print("\\")

# Multiply string with int
print("Hello"*5)

# Reconvert string to int
int('5')

# Split Mississippi by ("i")
Mississippi = "Mississippi"
Mississippi.split("i")

# Split German words
word = "Geräuschkulisse"
word.split("ä") # works fine


###### Exercise 3: #-------------------------#
# Create a string that, when indexed by [3::2] gives the string 'easter egg'
string = "abceeagsitkemro qesggg"
string[3::2]

###### Exercise 4: #-------------------------#
# Even or odd?
num = eval(input("Give me a number:" ))
if (num % 2 == 0):
    print("You gave me an even number.")
else:
    print("Huh, that's odd...")
    
# Fibonacci
num = int(input("Give me a number:" ))
svv = 0
sj = 1
j = 0
sv = 0
while num > j:
    if (sv == 0):
        print(sv)
        j = j + 1
        print(sj)
        sv = sj + svv
        j = j + 1
    else:
        sj = svv + sv
        print(sj)
        e = sv
        sv = sj
        svv = e
        j = j+1
else: print("That is ", num, "'s Fibonacci sequence.")

# Changing characters
word = "pot"
print(word)
e = word[0]
f = word[-1]
main = word[1:-1]
print(f + main + e)

# Right numbers
num = [1,2,3,4,5]
my = [1,2,3]
if str(my).strip("[]") in str(num).strip("[]"):
    print("Nice, you have '123' in your sequence!")
else:
    print("Your sequence is inferior!")

# Dictionary of i*i
num = int(input("Give me a number:" ))
ndict = {}
i = 0
while i in range(num+1):
    ndict[i] = i*i
    i = i + 1
else:
    print(ndict)


###### Exercise 5: #-------------------------#
# Palindrome?
word = "hannah"
if word == word[::-1]:
    print("Palindrome.")
else:
    print("nope")

# The last word
word = input("Give me a sentence:" )
print(word.rsplit(' ', 1)[1])

# RPS
items = ["rock", "paper", "scissors"]
p1 = input("Choose 'rock', 'paper', or 'scissors':" )
while p1 not in items:
    p1 = input("P1, decide for 'rock', 'paper', or 'scissors', please:" )
else:
    p2 = input("Choose 'rock', 'paper', or 'scissors':" )
    while p2 not in items:
        p2 = input("P2, decide for 'rock', 'paper', or 'scissors', please:" )
    else:
        if p1 == p2:
            print("Tie")
        elif p1 == "rock":
            if p2 == "paper":
                print("Player 2 wins!", p1, "vs.", p2)
            else:
                print("Player 1 wins!", p1, "vs.", p2)
        elif p1 == "paper":
            if p2 == "scissors":
                print("Player 2 wins!", p1, "vs.", p2)
            else:
                print("Player 1 wins!", p1, "vs.", p2)
        elif p1 == "scissors":
            if p2 == "rock":
                print("Player 2 wins!", p1, "vs.", p2)
            else:
                print("Player 1 wins!", p1, "vs.", p2)
        else:
            print("No idea what is goint on")
        
# List of squared values from 1 to 20
nlist = []
i = 0
m = 20
while i in range(m+1):
    x = [i, i*i]
    nlist.append(x)
    i = i + 1
else:
    print(nlist)


###### End of script. #-------------------------#

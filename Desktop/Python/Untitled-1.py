print("Hello, world!")
print("What is you name")
myName = input()
print ("It is good to meet you " + myName)
print ("The length of your name is:")
print (len(myName))
print ("What is your age?")
myAge = input()
print ("You will be " + str(int(myAge) + 1) + " in a year.")

while True:
    print ("Please restate your name")
    name = input() 
    if myName.lower() != name.lower():
        print("Who are you fooling around with? ")
    elif name.lower() != 'mary':
        print ("You can't continue cause you don't own this")
        quit()
    else:
        if name.lower() == 'mary':
            print ("Hello, Mary")
            break


print("What is the password, Mary?")
password = input()
if password == 'swordfish':
      print('Access granted.')
else:
      print('Wrong password. Access denied.')


if password == 'swordfish' and myName.lower() == 'mary':
  print('Hi, Mary.')
elif int(myAge) < 12:
  print('You are not Mary, kiddo.')
elif int(myAge) > 70:
  print('You are not Mary, granny.')
else:
  print('You are not Mary, nor a kid. Shame!')

quit()
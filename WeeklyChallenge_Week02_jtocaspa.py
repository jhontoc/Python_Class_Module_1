print('Hi my name is Python Bot...')
print('I would like to ask you some questions for my survery')
selector=input("are you ready to start, Yes or No?\t")
while selector=='Yes':
    name=input('1.- what is your name:\t')
    try:
        age=int(input('2.- what is your age:\t'))
        email=input('3.- what is your full email address:\t')
        PI=float(input('4.- what is the PI value:\t'))
    except ValueError:
        print('this is not a whole number, try again')
        continue

    print("Finally, the last question.. be patient \n")
    _address=str(input('5.- where do you live?:\t'))
    print ("thank you, " + name + " below is your personal information\n")
    print("your personal information {} , age {} , address:{}, email {}, PI {} ".format(name, age,_address,email,PI))
    break
else:
    print ("we will be doing in another time :(")

    






bgp
copp policy



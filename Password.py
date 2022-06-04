from random import *
password = input("Enter a password : ".lower().strip())
my_password = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

while my_password != password:
    my_password = ""
    for i in password:
        guss_letter = letters[randint(0, 25)]
        my_password = str(guss_letter) + str(my_password)
        # print(my_password)
        if my_password == password:
            print("The Password is Cracked!")
            print("The Password is => ", my_password)

            break








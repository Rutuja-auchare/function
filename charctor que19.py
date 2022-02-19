def number():
    num=input("enter the letter or digit:")
    if num>="A" and num<="Z":
        print(num,"alphabetic upper case leeter:")
    elif num>="a" and num<="z":
        print(num,"lower case leeter:")
    elif num>="0" and num<="9":
        print(num,"digit")
    else:
        print(num,"special chatretor")
number()    

try :
    num = int(input("Enter your number :"))
    print(num)
except ValueError as ex:
    print("exception" , ex)


print("I am outside the try block")
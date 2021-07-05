#Health Management System
import datetime
def getdate():
    return datetime.datetime.now()
def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c = int(input("Enter a food for exercise 1 and 2 for food "))
        if(c==1):
            value=(input("Type here\n"))
            with open("yash.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("sucessfully written")
        elif(c==2):
            value = (input("type here\n"))
            with open("yash-food.txt","a") as op:
                op.write(str([str(gettime())]) + ": "+value+"\n")
            print("sucessfully written")
    elif(k==2):
        c = int(input("enter 1 for exercise and 2 for food "))
        if(c==1):
            value = (input("type here\n"))
            with open("yash2.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("sucessfully written")
        elif(c==2):
            value = input("type here\n")
            with open("yash2-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

    elif(k==3):
        c=int(input("enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = (input("type here\n"))
            with open("yash3.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("yash3-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

        else:
            print("plz enter valid input (1(yash),2(yash2),3(yash3)")

def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("yash.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c == 2):
            with open("yash-food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("yash2.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("yash2-food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("yash3.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("yash3-food.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("plz enter valid input (yash,yash2,yash3)")

print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for yash 2 for yash2 3 for yash3 "))
    take(b)
else:
    b = int(input("Press 1 for yash 2 for yash2 3 for yash3 "))
    retrieve(b)




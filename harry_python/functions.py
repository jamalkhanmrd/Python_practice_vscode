# function for geometric mean
def gmean(a,b):
    geomean=(a*b)/(a+b)
    print("Geometric mean:",geomean)
a=5
b=7
gmean(a,b)
def isgreate(a,b):
    if (a>b):
        print("First number is greater than second")
    else:
        print("second number is greater than first")

a=5
b=4    
isgreate(a,b)



# functions arguments in py
def average(a,b):
    print("the average is :",(a+b)/2)

average(4,5)


# defult arguments
def average(a=4,b=5):
    print("the average is :",(a+b)/2)

# average(4,5)
average()

# argument as tuple
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))
average(4,5)


# argument as dictionary
def name(**name):
    print("Hello,",name["fname"],
          name["mname"],name["lname"])

name(mname="akmal",lname="ahmed",fname="ali")




# return
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(4,5)
print("Ave",c)


def add(a=5,b=5):
    return a+b

def sub(a=5,b=5):
    return a-b

def mul(a=5,b=5):
    return a*b

def div(a=5,b=5):
    return a/b 
    
a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter your choice \n1.add\n2.sub\n3.mul\n4.div"))
match c:
 case 1:print("sum of no's = ",add(a,b))
 case 2:print("sub of no's = ",sub(a,b))
 case 3:print("mul of no's = ",mul(a,b))
 case 4:print("div of no's = ",div(a,b))
 case _:print("wrong choice")

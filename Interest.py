
def SI():
    print("Find out SI with Amount")
    x=float(input('Principle:'))
    y=float(input("Rate: "))
    z=float(input("Time: "))


    si=(x*y*z)/100

    print("SI = Rs",si)
    print("Amount: Rs ",x+si)

def CI():
    print("Find out CI with Amount")
    x=float(input("Principle:"))
    y=float(input("Rate:"))
    z=int(input("Time(Years):"))
    w=float(input("Time(Months(If not, enter 0)))"))
    if w>0:
        mon_si=x*(1+y/100)**z
        mon_s2=(mon_si*y*w)/100
        print("CI : Rs ",mon_s2)
        print("Amount : Rs ",mon_s2+x)
    elif (w==0):
        amount=x*(1+y/100)**z
        print("Amount: Rs ",amount)
        print("CI: Rs", amount-x)

while True:        
    Option = input("Select the function you want to use(CI for Compound Interest or SI for Simple Interest) :")

    if Option == "CI"or"ci":
        CI()
        break
    elif Option == "SI"or"si":
        SI()
        break
    else:
        print("Error:Select an appropriate option.")





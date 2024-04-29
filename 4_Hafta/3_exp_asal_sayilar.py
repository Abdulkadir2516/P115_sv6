import datetime

start,stop= 0,100000 #input("2 sayı aralığı girin 5-15: ").split("-")
print(datetime.datetime.now())

start,stop = int(start),int(stop)

def asalmi(number):

    for i in range(2,int(number/2)+1):
        if number%i == 0:
            return False

    return True

s = 0
for i in range(start,stop+1):
    if asalmi(i):
        print(i, end=" ")
        s +=1
        if s%10 == 0:
            print()

    #if s == 100:
    #    exit()




print(datetime.datetime.now())








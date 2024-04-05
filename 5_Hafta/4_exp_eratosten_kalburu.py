import datetime

print(datetime.datetime.now())

a_dizisi = list(range(2,100000)) #n

prime_numbers = [] # 1 n^2

for k,i in enumerate(a_dizisi): # n
    prime_numbers.append(i) # 1
    print(i) # 1
    for j in a_dizisi[k+1::]: # n/2 /
        if j % i == 0: # 1
            a_dizisi.remove(j) # 1

print(prime_numbers)
print(a_dizisi)

print(datetime.datetime.now())

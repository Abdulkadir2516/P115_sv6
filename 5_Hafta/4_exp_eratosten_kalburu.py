import datetime

print(datetime.datetime.now())

prime_numbers = list(range(2,100))

for k,i in enumerate(prime_numbers):
    print(i)
    if i**2 in prime_numbers:

        for j in prime_numbers[prime_numbers.index(i**2)::]:
            if j % i == 0:
                prime_numbers.remove(j)

print(prime_numbers)
print(len(prime_numbers))

print(datetime.datetime.now())

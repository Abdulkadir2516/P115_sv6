# İf Else Elif
# Eğer ise, Değil ve Eğer değilse


#Python program to find maximum between three numbers
# klasik if else yöntemi

import random as rnd

num1, num2, num3 = rnd.randint(a=1,b=200),rnd.randint(a=1,b=200),rnd.randint(a=1,b=200)


#num1 48 > num2 26 > num3 5

if num1 > num2 and num1 > num3:
    print(num1, end=" > ")

    if num2 > num3:
        print(num2, end=" > ")
        print(num3)
    else:
        print(num3, end=" > ")
        print(num2)
elif num2 > num1 and num2 > num3:
    print(num2, end=" > ")

    if num1 > num3:
        print(num1, end=" > ")
        print(num3)
    else:
        print(num3, end=" > ")
        print(num1)
elif num3 > num1 and num3 > num2:
    print(num3, end=" > ")

    if num1 > num2:
        print(num1, end=" > ")
        print(num2)
    else:
        print(num2, end=" > ")
        print(num1)

# ileri yöntem

rastgele_listem = [rnd.randint(a=1,b=200) for i in range(10)]
print(rastgele_listem)

for i in range(len(rastgele_listem)-1):
    print(max(rastgele_listem), end=" > ")
    rastgele_listem.remove(max(rastgele_listem))
print()
# daha ileri yöntem


numbers = [rnd.randint(1, 200) for _ in range(3)]
numbers.sort(reverse=True)

print(" > ".join(map(str, numbers)))





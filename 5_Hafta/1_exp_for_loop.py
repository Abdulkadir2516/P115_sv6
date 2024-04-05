dizi = list(range(10))

dizi2 = [i for i in range(10) if i%2 == 0 ]

print(dizi2)

dizi3 = []

for i in range(10):
    if i%2 == 0:
        dizi3.append(i)
print(dizi3)

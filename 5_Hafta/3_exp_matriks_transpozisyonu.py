

dizi = []
d = []

for i in range(1,26):
    d.append(i)
    if i%5 ==0:
        dizi.append(d)
        d = []


# dizi = [[1, 2, 3, 4, 5],
# [6, 7, 8, 9, 10],
# [11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20],
# [21, 22, 23, 24, 25]
# ]

dizi_t = []

for i in range(len(dizi)):
    k = []
    for j in range(5):
        print(dizi[j][i], end=" " )
        k.append(dizi[j][i])
    dizi_t.append(k)
    print()

print(dizi_t)

#Yöntem 2

dizi = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
sutunlar = [[dizi[a][i] for a in range(len(dizi))] for i in range(len(dizi[0]))]
print("tranpos = "+str([i for i in sutunlar ]))
liste1 = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
liste2 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

print(list(set(liste1).difference(liste2)) +list(set(liste2).difference(liste1)))





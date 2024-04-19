

# 4 tip fonksiyon var:
# 1- parametre alan geri değer döndüren
def my_func1(a):
    return f"hello word {a}"

# 2- parametre alan geri değer döndürmeyen
def my_func2(a):
    print("hello word", a)

# 3- parametre almayan geri değer döndüren
def my_func3():
    return "hello word"

# 4- parametre almayan geri değer döndürmeyen
def my_func4():
    print("hello word")


print(my_func1(5))

my_func2(5)

print(my_func3())
my_func4()

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(child3, child2="null", child1="null"):
    print("The youngest child is " + child3)
    print("The youngest child is " + child2)
    print("The youngest child is " + child1)


my_function("Emil", "Tobias", )

def my_function(*kids):
    for i in kids:
        print(i)

my_function("Emil", "Tobias", "Linus","merb",",dvsfgs","fesfsfe4w","gfdgg4er","erhgebe","gerervre","vregh")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# print(help(range))

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

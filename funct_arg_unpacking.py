# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

if __name__ == "__main__":

    print("Example 1")
    myfunc(*tuple_vec)

    print("Example 2")
    myfunc(**dict_vec)

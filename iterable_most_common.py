# collections.Counter lets you find the most common
# elements in an iterable:
import collections
c = collections.Counter('helloworld')

if __name__ == "__main__":
    print((c.items()))
    print()
    print()
    for item in c.items():
        if item[1] > 1:
            print("Not an isogram")
            break
    else:
        print("Is an isogram")
    print()
    print()    
    print(f"Counted iterables are {c}")
    print()
    print()
    print(f"The most ommon items are {c.most_common(3)}")
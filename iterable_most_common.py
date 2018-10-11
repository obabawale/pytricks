# collections.Counter lets you find the most common
# elements in an iterable:
import collections
c = collections.Counter('helloworld')

if __name__ == "__main__":
    
    print(f"Counted iterables are {c}")

    print(f"The most ommon items are {c.most_common(3)}")
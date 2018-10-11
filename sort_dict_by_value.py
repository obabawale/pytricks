# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

if __name__ == "__main__":   

    print("using anonymous fuunction with `sorted()`", sorted(xs.items(), key=lambda x: x[1]))

    # Or:

    import operator
    print("using operator.itemgetter()", sorted(xs.items(), key=operator.itemgetter(1)))

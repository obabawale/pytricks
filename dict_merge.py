# -*- encoding: utf-8 -*-

############################################################################
# Merge two dictionaries without using the usual the common update() method
############################################################################

dict_1 = dict(name="Adewale", sex="Male")
dict_2 = dict(color="chocolate", height=234)
dict_3 = dict(tribe="Delta", soo="Ondo")

dict_merge = {**dict_1, **dict_2, **dict_3}

if __name__ == "__main__":
    print(f"The merger of all the dicts is:\n{dict_merge}")

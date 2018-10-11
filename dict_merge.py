# -*- encoding: utf-8 -*-

############################################################################
# Merge two dictionaries without using the usual the common update() method
############################################################################

dict_1 = dict(name="Adewale", sex="Male")
dict_2 = dict(color="chocolate", height=234)
dict_3 = dict(tribe="Delta", origin="Ondo")

def main(dict_1=dict_1, dict_2=dict_2, dict_3=dict_3):
    """Return combined values of different dictionaries"""
    dict_merge = {**dict_1, **dict_2, **dict_3}
    return dict_merge

if __name__ == "__main__":
    print(f"The merger of all the dicts is:\n{main()}")

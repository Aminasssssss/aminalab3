import itertools

def string_permutations(s):
    return list(map("".join, itertools.permutations(s)))

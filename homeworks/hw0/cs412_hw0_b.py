"""Coding Homework 0: Basic Algorithms.

    Dictionary implementation.

    The first thing that I changed was my dictionary assignment 
    on line 30. Not using dict.update() and directly 
    assigning keys and values speeds up my code by about half.
    I also moved my 'fox' and 'known' variable declarations 
    to the top of my code because when it was in the middle, 
    it was getting hit an unreasonable amount of times (it 
    just needed to be 1)

    Name:  Adrien Ponce
    Honor Code: This code complies with the JMU Honor Code.
"""


@profile
def main():
    noises = input().split() # look for subs for .split()
    n = int(input())
    # map for animal sounds
    animals = {}
    # store fox and 'known' sounds
    fox = []
    known = {}
    for _ in range(n):
        heard = input().split()
        # k = sound, v = animal
        animals[heard[2]] = heard[0]
    # store fox and 'known' sounds
    # fox = []
    # known = {}
    for noise in noises:
        # known noise found
        if noise in animals:
            # add known reference (auto no duplicates)
            # known.update({animals.get(noise) : None})
            known[animals.get(noise)] = None
        else:
            # noises not known are 'foxes'
            fox.append(noise)
    # output solution 
    print("what the fox says:", *fox, "")
    print("also heard:", *known, "")


if __name__ == "__main__":
    main()

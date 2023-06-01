"""Coding Homework 0: Basic Algorithms.

    List implementation.

    Name:  Adrien Ponce
    Honor Code: This code complies with the JMU Honor Code.
"""


def main():
    noises = input().split()
    n = int(input())
    # create parallel mapping arrays
    animal = []
    sound = []
    # populate array
    for _ in range(n):
        heard = input().split()
        # 'map' animal and its sound
        # k = sound, v = animal
        animal.append(heard[0])
        sound.append(heard[2])
    # store fox and 'known' sounds
    fox = []
    known = []
    for noise in noises:
        # known noise found
        if noise in sound:
            # key search for animal
            key = sound.index(noise)
            # avoids duplicate animals
            if animal[key] not in known:
                known.append(animal[key])
        # noises not known are 'foxes'
        else:
            fox.append(noise)   
    # output solution 
    # (hopefully fixes whitespace errors, 
    # .join() adds extra whitespace))
    print("what the fox says:", *fox, "")
    print("also heard:", *known, "")


if __name__ == "__main__":
    main()

"""Coding Homework 4: Dynamic Programming I.

    Dynamic programming algorithm that counts the 
    minimum number of rocket sections needed to build 
    a rocket of length n using input from stdin.

    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def min_needed(sections, target):
    """ These functions returns a tuple containing
    the minimum sections needed for a rocket of 
    length target, where length is the remaining
    target left to go."""
    def find_min(length):
        # invalid length, return 'nothing'
        if length < 0:
            return float('+inf'), []
        # base case, finished and go back up
        if length == 0:
            return 0, []
        # check that desired length has not been computed
        if length not in cache:
            # stores an int min count and arr sections used
            min_count = float('+inf')
            min_used = []
            # go through each section starting at
            # the end (to avoid max recur depth)
            for i in range(len(sections) - 1, -1, -1):
                # count is min, used is build of curr length
                count, used = find_min(length - sections[i])
                # update min if curr count is lower than before
                if count + 1 < min_count:
                    min_count = count + 1
                    min_used = used + [sections[i]]
                    # store tuple of min count and arr
                    # of used sections in the cache
                    cache[length] = (min_count, min_used)
        # return min count and build needed for length
        return cache[length]
    cache = {}
    return find_min(target)


def main():
    tmp = input().split()
    sections = []
    # build list of sections
    for i in range(len(tmp)):
        sections.append(int(tmp[i]))
    n = int(input())
    result = min_needed(sections, n)
    # formatting output
    for i in range(len(sections)):
        if sections[i] in result[1]:
            print(result[1].count(sections[i]), "of length", sections[i])
        else:
            print("0 of length", sections[i])
    print(result[0], "rocket sections minimum")


if __name__ == "__main__":
    main()

"""Coding Homework 3: Backtracking.

    Recursive backtracking algorithm that counts the 
    minimum number of rocket sections needed to build
    a rocket of length n.

    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def min_sections(sections, target):
    # start min cuts at curr target val
    min = target
    built = []
    # target reached, go back up tree
    if target == 0 or target in sections:
        # need to return min and section used
        return 1, [target]
    else:
        for section in sections:
            if section < target:
                # count is for min, curr is section used
                count, curr = min_sections(sections, target - section)
            # need to obtain the min 'cut' count
            if count + 1 < min:
                min = count + 1
                # add curr arr to arr of built sections
                built = curr + [section]
    return min, built


def main():
    tmp = input().split()
    sections = []
    # build list of sections
    for i in range(len(tmp)):
        sections.append(int(tmp[i]))
    n = int(input())
    min, built = min_sections(sections, n)
    # formatting
    for num in sections:
        print(built.count(num), "of length", num)
    print(min, "rocket sections minimum")


if __name__ == "__main__":
    main()

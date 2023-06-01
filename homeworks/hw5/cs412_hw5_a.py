""" Coding Homework 5: Dynamic Programming II.
    
    Iterative dynamic programming algorithm that
    counts the minimum number of rocket sections 
    needed to build a rocket of length n using 
    input from stdin.

    Name: 
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def min_needed(sections, target):
    """ Cache stores a dictionary of a minimum count
        that has a tuple containing the sections that 
        were added to the build. """
    cache = {0: (0, [])}
    # The outer loop is the solution building phase.
    for length in range(1, target + 1):
        min_count = float('+inf')
        min_build = []
        # The inner loop is the dynamic programming phase.
        for section in sections:
            remaining = length - section
            # The remaining section length has not yet reached the target.
            if remaining >= 0 and remaining in cache:
                # Store the current minimum
                count, used = cache[remaining]        
                # Update the minimum count and build
                if count + 1 < min_count:
                    min_count = count + 1           
                    min_build = used + [section]  
        cache[length] = (min_count, min_build)
    return cache[target]


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

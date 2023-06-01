"""Lab 4: Dynamic Programming I

    Modified version of lab 3 indices
    and an array to store used values.

    Name: 
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


"""Returns true if string is a palindrome.
    We also need to rebuild the string."""
def is_palindrome(string, start, end):
    result = string[start:end+1]
    return result == result[::-1]


"""Return min number of palindromic partitioning
    of a string."""
def partition_outer(string):
    def partition(index):
        # base case, go back up tree with 1
        if len(string) == index:
            return 1
        else:
            count = 0
            # go through entire substring
            for i in range(index, len(string)):
                # if beginning half of substring is palindrome
                if is_palindrome(string, index, i):
                    # check that index DNE in cache
                    if cache[index] is None:
                        # check the end half for palindromes to partition
                        count += partition(i + 1)
                    # index exists in cache, return immediately
                    else:
                        return cache[index]
            # store computed value at used starting index
            cache[index] = count
            return count
    # used to store computed counts
    cache = [None for _ in range(len(string)+1)]
    return partition(0)


def main():
    n = int(input())
    for _ in range(n):
        query = input()
        print(partition_outer(query))
          

if __name__ == "__main__":
    main()

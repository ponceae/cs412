"""Lab 4: Dynamic Programming I

    Modified version of lab 3 using a 
    dictionary to store used values.

    Name: 
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


"""Returns true if string is a palindrome."""
def is_palindrome(string):
    return string == string[::-1]


"""Return min number of palindromic partitioning
    of a string."""
def count_pp(query):
    def count_palindrome_parts(string):
        # base case, go back up tree with 1
        if len(string) == 0:
            return 1
        else:
            count = 0
            # go through entire substring
            for i in range(len(string)):
                # if beginning half of substring is palindrome
                if is_palindrome(string[:i+1]):
                    # check that substring DNE in cache
                    if cache.get(string) is None:
                        # check the end half for palindromes to partition
                        count += count_palindrome_parts(string[i+1:]) 
                    # substring exists in cache, return immediately
                    else:
                        return cache.get(string)
            # map the substring to the computed value
            cache[string] = count
            return count
    # used to store computed counts
    cache = {}
    return count_palindrome_parts(query)


def main():
    n = int(input())
    for _ in range(n):
        query = input()
        print(count_pp(query))
          

if __name__ == "__main__":
    main()

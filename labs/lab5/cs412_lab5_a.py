"""Lab 5: Dynamic Programming II.

    Another take on the palindromic partitioning
    problem using bottom-up dynamic programming
    (i.e., no recursion).

    Runtime Analysis:
        - Line 23 takes O(n) time. 
        - The loops on line 29-31 takes O(n^2) time
        - The is_palindrome function takes O(n) time,
          bringing the loop total to O(n^3) time.
        - All other operations take O(1) time.
        - Therefore, O(n) + O(n^3) + O(1) + O(1) = 
                    O(n^3) + n
    
    Name:
        Adrien Ponce
    Honor Code: 
        This code complies with the JMU Honor Code.
"""


def is_palindrome(string):
    return string == string[::-1]


def partition(query, size):
    # used to store partitions of each substring
    cache = [0] * (size + 1)
    # sentinel cell for empty string 
    cache[size] = 1   
    # iterate backwards through input string
    for i in range(size - 1, -1, -1):
        # iterate through substring 
        for j in range(i + 1, size + 1):
            # substring is a palindrome
            if is_palindrome(query[i:j]):
                # update curr cell based on value to
                # the right of it
                cache[i] += cache[j]   
    return cache[0]


def main():
    n = int(input())
    for _ in range(n):
        query = input()
        print(partition(query, len(query)))


if __name__ == "__main__":
    main()

"""Lab4: Dynamic Programming II

    Name: 
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def palindrome(word):
    return word == word[::-1]


def partition_outer(word):
    def partition(start):
        # base case, go back up tree with 1
        if len(word[start:]) == 0:
            return 1
        else:
            count = 0
            # go through entire substring
            for i in range(len(word[start:])):
                # if beginning half of substring is palindrome
                if palindrome(word[:start]):
                    if cache.get(word[start:]) is None:
                        # check the end half for palindromes to partition
                        count += partition(i+1) 
                    else:
                        return cache.get(word[start:])
            cache[word[start:]] = count
            return count
    cache = {}
    return partition(len(word))


def main():
    n = int(input())
    for _ in range(n):
        word = input()
        print(partition_outer(word))
          

if __name__ == "__main__":
    main()

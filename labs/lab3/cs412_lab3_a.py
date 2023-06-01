"""Lab 4: Backtracking 

    Recursive backtracking algorithm that counts the 
    number of palindromic partitions of a given string.
    
    Name:  
        Adrien Ponce
    Honor Code: 
        This code complies with the JMU Honor Code.
"""


def palindrome(str):
    return str == str[::-1]


def partition(str):
    # base case, go back up tree with 1
    if len(str) == 0:
        return 1
    else:
        count = 0
        # go through entire substring
        for i in range(len(str)):
            # if beginning half of substring is palindrome
            if palindrome(str[:i+1]):
                # check the end half for palindromes to partition
                count += partition(str[i+1:]) 
        return count


def main():
    n = int(input())
    for _ in range(n):
        word = input()
        print(partition(word))
          

if __name__ == "__main__":
    main()

"""Lab 0: Python Intro
    Name:  Adrien Ponce
    Honor Code: This code complies with the JMU Honor Code.
    Lab Questions:
    1.) What data structures did you use? 
            I used a dictionary and a list.
    2.) What data structure operations did you use? (List all of them.)
            I used split(), append(), get(), and join().
    3.) Assuming a data structure of size n, what is the runtime of each of 
        the operations you identified above? 
            I have two for loops, which take O(2n) or just O(n) time. split() goes 
            through every whitespace in the string, taking O(n) time. append() 
            takes constant O(1) time, get() takes O(n) in the worst case since you 
            might have to go through the whole dictionary, and join() takes O(n) 
            time since it has to add whitespace after each element.
    4.) What is the runtime of your algorithm?
            Adding all of the above, it brings me to a total runtime of just O(n).
    5.) Why does your algorithm work?
            First I have to gather input from a .txt file, so I just use a loop to go 
            through the first n lines which I build my dictionary with. Once 
            constructed, I save the message that is to be translated. Lastly, I use 
            an array to store the translated words. Once the words have been looked 
            up in the dictionary, I output the corresponding translated word. 
"""


def main():
    # num words in dictionary
    n = int(input())
    lookup = {}
    for _ in range(n):
        line = input().split()
        lookup[line[1]] = line[0]
    # message to be translated
    message = input().split()
    # hold the answer
    sol = []
    # lookup translations
    for word in message:
        sol.append(lookup.get(word, "???"))
    # solution output
    print(" ".join(sol), end=" ")
    print()
        

if __name__ == "__main__":
    main()

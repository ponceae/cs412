""" Lab 13: NP-Completeness Part B

    Name: 
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""
import itertools


def evaluate(x):
    x1, x2, x3 = map(bool, x)
    return ((not x1 or not x2 or not x3) and (x1 or not x2 or not x3)
    and (not x1 or not x2 or x3) and (not x1 or x2 or not x3) 
    and (not x1 or x2 or x3) and  (x1 or not x2 or x3)
    and (x1 or x2 or not x3) and  (x1 or x2 or x3))


def evaluate_missing(x):
    x1, x2, x3 = map(bool, x)
    return ((x1 or not x2 or not x3)
    and (not x1 or not x2 or x3) and (not x1 or x2 or not x3) 
    and (not x1 or x2 or x3) and  (x1 or not x2 or x3)
    and (x1 or x2 or not x3) and  (x1 or x2 or x3))

def main():
    for vals in itertools.product([True, False], repeat=3):
        print(vals)

    for vals in itertools.product([True, False], repeat=3):
        result = evaluate(vals)
        if not result:
            print(vals, result)
    
    for vals in itertools.product([True, False], repeat=3):
        result = evaluate_missing(vals)
        if result:
            print(vals, result)


if __name__ == "__main__":
    main()

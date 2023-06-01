""" Lab 6: Greedy Algorithms, Part B: Fractional Knapsack.

    This algorithm takes a weight W and a list of items that 
    can be put into the knapsack, with each item having a particular 
    weight and associated price. When space has run out of the sack, 
    then the algorithm fractionalizes the item based on its price
    to weight ratio and tries to re-insert it into the sack.

    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def fractional_knapsack(items, W):
    """ Where:
                 W  = bag capacity
            item[0] = item name
            item[1] = price
            item[2] = weight
    """
    # Sort the items in descending order based on its price
    items.sort(key = lambda x:x[1] / x[2], reverse = True)
    plunder = 0.0   # Keeps track of total knapsack value
    i = 0
    while i < len(items):
        item = items[i]
        # Item will fit into the knapsack.
        if item[2] <= W:        
            print(item[0], end="(") 
            print("{:.2f},".format(item[1]), "{:.2f}".format(item[2]), end=") ")
            W -= item[2]        # Update remaining weight
            plunder += item[1]  # Update count 
        # Item will not fit into the sack.
        else:
            ratio = W / item[2]         # Ratio = price / weight
            new_price = ratio * item[1] # Adjust price w/ respect to ratio
            if ratio != 0 and new_price != 0:
                print(item[0], end="(") 
                print("{:.2f},".format(new_price), "{:.2f}".format(W), end=")\n")
                plunder += new_price        # Update count
                break
        i += 1
    return plunder



def main():
    W = int(input())
    n = int(input())
    items = []
    # obtain available items
    for _ in range(n):
        item = input().split()
        # use a tuple to 'map' item to its corresponding attributes
        items.append((item[0], float(item[1]), float(item[2])))
    print(fractional_knapsack(items, W), end="\n")


if __name__ == "__main__":
    main()

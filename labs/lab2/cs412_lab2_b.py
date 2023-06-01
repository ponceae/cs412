"""Lab2: Recursive Algorithms.

    Part B: Inversions.

    Name:  
        Adrien Ponce 
    Honor Code and Acknowledgements: 
        This code complies with the JMU Honor Code.
        The code for Mergesort was provided by 
        Professor Bowers.
"""


def mergesort(A):
    ctr = 0
    if len(A) > 1:
        # Get the mid point
        m = len(A) // 2
        # Get the left and right halves
        left, right = A[:m], A[m:]
        # sort the left and right halves
        # (one off error if ctr not updated here)
        ctr += mergesort(left)
        ctr += mergesort(right)

        # Copy the sorted left and right halves back to A. 
        for i in range(m):
            A[i] = left[i]
        for j in range(m, len(A)):
            A[j] = right[j - m]  
        # Run the merge operation on A 
        # and update the inversion count
        ctr += merge(A, m)
    return ctr


def merge(A, m):
    ctr = 0
    i, j = 0, m
    n = len(A)
    B = [0 for _ in range(n)]
    for k in range(n):
        if j >= n:
            B[k] = A[i]
            i += 1
        elif i >= m:
            B[k] = A[j]
            j += 1
        elif A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            # update inversion count
            # (keeps track of 'jumps')
            ctr += (m - i)
            B[k] = A[j]
            j += 1
    for k in range(n):
        A[k] = B[k]
    return ctr


# reads input from stdin
def main():
    inp = input().split()
    list_input = []
    for i in range(len(inp)):
        list_input.append(int(inp[i]))
    print(mergesort(list_input))


if __name__ == "__main__":
    main()
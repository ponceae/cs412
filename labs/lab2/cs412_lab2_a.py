"""Lab2: Recursive Algorithms.

    Part A: Circular search.

    Name:  
        Adrien Ponce
    Honor Code: 
        This code complies with the JMU Honor Code.
"""


# binary search for a circularly sorted array
def circular_search(nums, q, left, right):
    # first base case, empty list or q does not exist
    if (left + right + 1 <= 1
            or q not in nums):
        return -1
    # midpoint for binary search
    mid = (left + right) // 2
    # element found, return index
    if nums[mid] == q:
        return mid

    # left subarray is sorted
    if nums[left] <= nums[mid]:
        # if index of q in bounds, index must be in left subarray
        if q in nums[left:mid+1]:
            return circular_search(nums, q, left, mid - 1)
        # else, index is in unsorted right subarray
        else:
            return circular_search(nums, q, mid + 1, right)
    # right subarray is sorted
    if nums[right] >= nums[mid]:
        # if index of q in bounds, index must be in right subarray
        if q in nums[mid:right+1]:
            return circular_search(nums, q, mid + 1, right)
        # else, index is in unsorted right subarray
        else:
            return circular_search(nums, q, left, mid - 1)


# reads input from stdin
def main():
    inp = input().split()
    list_input = []
    for i in range(len(inp)):
        list_input.append(int(inp[i]))
    query = int(input())
    print(circular_search(list_input, query, 0, len(list_input) - 1))


if __name__ == "__main__":
    main()
    
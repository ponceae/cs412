"""Coding Homework 1: Dual Stacks.

    Python class that creates a dual stack using an
    underlying list data structure.

    Name:  Adrien Ponce
    Honor Code: This code complies with the JMU Honor Code.
"""


class TwoStack:

    # creates two empty stacks stored in a single underlying
    # list with length 2
    def __init__(self):
        self.stacks = [None] * 2
        # head of L stack
        self.t1 = -1
        # len of underlying array
        self.cap = len(self.stacks)
        # head of R stack
        self.t2 = self.cap
        # init stack sizes
        self.size1 = 0
        self.size2 = 0

    # return underlying array capacity
    def capacity(self):
        return self.cap  

    # copies old values into new array after growing
    def grow_copy(self, tmp, ptr, ctr):
        # copy L stack
        for i in range(self.size1):
            tmp[i] = self.stacks[i]
        # update head of stack2
        self.t2 = ptr

        # copy R stack
        for _ in range(len(self.stacks) - 1, self.size1 - 1, -1):
            tmp[ptr] = self.stacks[ctr]
            # DO NOT CHANGE BELOW, SOMEHOW WORKS
            ptr += 1
            ctr += 1
        # finalized copy
        self.stacks = tmp

    # double the size of the list
    def grow_list(self):
        # adjusted 'jump' pointer 
        ptr = self.t2 + self.cap
        # counter for old list
        ctr = self.t2
        # create new x2 list
        self.cap *= 2
        tmp = [None] * self.cap
        self.grow_copy(tmp, ptr, ctr)  

    # return len of stack1    
    def size1(self):
        return self.size1

    # return len of stack2
    def size2(self):
        return self.size2

    # removes all elements from stack1
    def clear1(self):
        # 'jump' stack pointer
        ptr = self.cap - (self.t2 - 1) 
        tmp = [None] * self.cap
        # copy R stack into new array
        for i in range(len(self.stacks) - 1, self.size1 - 1, - 1):
            tmp[ptr] = self.stacks[i]
            ptr -= 1
            # update stack pointer
            self.t2 = i
        # reflect empty stack changes
        self.size1 = 0

        # check if shrink needed, half it if needed
        if (self.cap != 2 
                and (self.cap - self.size1 <= self.cap // 2)):
            self.cap = self.cap // 2
            self.stacks = self.shrink_copy(tmp)
        # this checks when the capacity wastes space
        while (self.cap != 2 
                and (self.cap // 2 >= self.size1 + self.size2)):
            self.cap = self.cap // 2
            self.stacks = self.shrink_copy(tmp)
        # treat stack1 as new empty stack
        self.t1 = -1

    # removes all elements from stack2
    def clear2(self):
        tmp = [None] * self.cap
        # copy L stack into new array
        for i in range(self.size1 - 1):
            tmp[i] = self.stacks[i]
        # reflect empty stack changes
        self.size2 = 0

        # check if shrink needed, half it if needed
        if (self.cap != 2 
                and (self.cap - self.size1 <= self.cap // 2)):
            self.cap = self.cap // 2
            self.stacks = self.shrink_copy(tmp)
        # this checks when the capacity wastes space
        while (self.cap != 2 
                and (self.cap // 2 >= self.size1 + self.size2)):
            self.cap = self.cap // 2
            self.stacks = self.shrink_copy(tmp)
        # treat stack2 as new empty stack
        self.t2 = self.cap - 1

    # push v onto stack1
    def push1(self, v):
        # check for available space
        if (self.t1 < self.t2 - 1):
            # update pointer
            self.t1 += 1
            self.stacks[self.t1] = v
            self.size1 += 1
        else:
            # double list size and retry insert
            self.grow_list()
            self.push1(v) 

    # push v onto stack2
    def push2(self, v):
        # check for available space
        if (self.t1 < self.t2 - 1):
            # update pointer
            self.t2 -= 1
            self.stacks[self.t2] = v
            self.size2 += 1
        else:
            # double list size and retry insert
            self.grow_list()
            self.push2(v) 

    # pop off of stack1
    def pop1(self):
        # empty stack exception
        if (self.size1 == 0 or self.t1 == -1):
            raise Exception("Error: EmptyStack")
        # extract element
        res = self.top1()
        # update spot where element popped
        self.stacks[self.t1] = None
        # update stack head and size
        self.t1 -= 1
        self.size1 -= 1

        # check if shrink needed, half it if needed
        if (self.cap != 2 
                and (self.cap - 1 <= self.cap // 2)):
            self.cap = self.cap // 2
            self.stacks = self.pop_copy(self.stacks)
        # this checks when the capacity wastes space
        if (self.cap != 2 
                and (self.cap // 2 >= self.size1 + self.size2)):
            self.cap = self.cap // 2
            self.stacks = self.pop_copy(self.stacks)
        return res

    # pop off of stack2
    def pop2(self):
        # empty stack exception
        if (self.size2 == 0 or self.t2 == self.cap):
            raise Exception("Error: EmptyStack")
        # sometimes the stack pointer is bigger than the capacity
        if (self.t2 >= self.cap):
            self.t2 = self.cap - 1
        # extract element
        res = self.top2()
        # update spot where element popped
        self.stacks[self.t2] = None
        # update stack head and size
        self.t2 += 1
        self.size2 -= 1
        
        # check if shrink needed, half it if needed
        if (self.cap != 2 
                and (self.cap - 1 <= self.cap // 2)):
            self.cap = self.cap // 2
            self.stacks = self.pop_copy(self.stacks)
        # this checks when the capacity wastes space
        if (self.cap != 2 
                and (self.cap // 2 > self.size1 + self.size2)):
            self.cap = self.cap // 2
            self.stacks = self.pop_copy(self.stacks)
        return res

    # copies elements into new array after a pop shrink
    def pop_copy(self, tmp):
        copy = [None] * self.cap
        i = 0
        ctr = 0
        # need both elements to be in bounds of old & new array
        while (i < len(copy) and ctr < len(tmp)):
            # avoids index out of bounds
            if (tmp[ctr] is not None):
                copy[i] = tmp[ctr]
                i += 1
            ctr += 1
        return copy

    # copies elements into new array after push grow
    def shrink_copy(self, tmp):
        copy = [None] * self.cap
        i = 0
        # iterate through smaller list
        while (i < len(copy)):
            copy[i] = tmp[i]
            i += 1
        return copy
    # return the element at sp1

    def top1(self):
        # empty L stack
        if (self.t1 == -1):
            raise Exception("Error: EmptyStack")
        return self.stacks[self.t1]

    # return the element at sp2
    def top2(self):
        return self.stacks[self.t2]
        
# misc tests
def main():
    # ts = TwoStack()
    # for i in range(1,21):
    #     ts.push1(i)
    # stack1_poplist = []
    # stack2_poplist = []
    # for i in range(101,121):
    #     ts.push2(i)
    # # print(ts.stacks)
    # for i in range(4):
    #     stack1_poplist.append(ts.pop1())
    #     stack2_poplist.append(ts.pop2())
    # # print(ts.stacks)
    # stack1_poplist.append(ts.pop1())
    # stack2_poplist.append(ts.pop2())
    # print(ts.stacks)
    # print("Expected:", [120, 119, 118, 117, 116], "Actual:", stack2_poplist)

    ts = TwoStack()
    for i in range(8):
        ts.push1(i)
    ts.push2(9)
    print(ts.stacks, ts.t2)
    ts.clear1()
    print(ts.stacks, ts.t2)

    print("Expected:", 2, "Actual:", ts.capacity())
    # print("Expected:", 9, "Actual:", ts.top2())


if __name__ == "__main__":
    main()

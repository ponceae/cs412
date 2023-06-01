import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from io import StringIO
from unittest.mock import patch

from cs412_hw1_a import TwoStack 

class TestHW1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass


    @weight(2)
    @number("1.2")
    def test_02(self):
        """Create a TwoStack and push 1 item on each stack"""
        ts = TwoStack()
        ts.push1('Kevin')
        ts.push2('Molloy')

        self.assertEqual(2,ts.capacity(), 
            "After two pushes, stack capacity should still be 2") 

        ts2 = TwoStack()
        ts2.push1("Kevin")
        ts2.push1("Molloy")

        self.assertEqual(2,ts2.capacity(), 
            "After two pushes, stack capacity should still be 2") 
        ts2 = TwoStack()
        ts2.push2("Kevin")
        ts2.push2("Molloy")

        self.assertEqual(2,ts2.capacity(), 
            "After two pushes, stack capacity should still be 2") 
        v1 = ts2.pop2()
        v2 = ts2.pop2()
        self.assertEqual("Molloy",v1, "First pop")        
        self.assertEqual("Kevin",v2, "First pop")        

               
    @weight(2)
    @number("1.3")
    def test_03(self):
        """Push 3 items and make sure list length is 4"""
        ts = TwoStack()
        ts.push2('1')
        ts.push2('2')
        ts.push2('3')
        # capacity should now be four
        self.assertEqual(4, ts.capacity(), 
            "After 3 pushes, stack capacity should  be 4")

    @weight(2)
    @number("1.4")
    def test_04(self):
        """Push 3 times and pop once, list length should shrink to 2"""
        ts = TwoStack()
        ts.push1('1')
        ts.push1('2')
        ts.push1('3')
        v = ts.pop1()
        # capacity should now go back to 2

        self.assertEqual(2, ts.capacity(), 
            "After 3 pushes and one pop, stack capacity should  be 2")

    @weight(2)
    @number("1.5")
    def test_05(self):
        """pushing and popping from both stacks -- checking pop returns"""
        ts = TwoStack()
        ts.push1(1)
        ts.push2(4)
        ts.push1(3)
        v = ts.pop1()
        
        # pop of stack 1 should yield a 3
        self.assertEqual(3, v, "Pop from stack 1 should yield a 3")

        # last pop should have caused the list to shrnk to size 2        
        self.assertEqual(2, ts.capacity(), 
            "After 3 pushes and one pop, stack capacity should  be 2")

        v = ts.pop2()

        self.assertEqual(4, v, "Pop of second stack should yield a 4")
        
        self.assertEqual(2, ts.capacity(), 
            "After 3 pushes and two pops, stack capacity should remain at 2")

    @weight(1)
    @number("1.6")
    def test_06(self):
        """Checking pushes and pops to both stacks and top function"""
        ts = TwoStack()
        for i in range(8):
            ts.push1(i)
        ts.push2(9)
        self.assertEqual(16, ts.capacity(), 
            "After 9 pushes, stack capacity should  be 16")
        self.assertEqual(9,ts.top2(), "Top of stack 2 should be a 9")
        self.assertEqual(9,ts.top2(), "Top should not change the stack" + \
            "(it just peeks)")

    @weight(2)
    @number("1.7")
    def test_07(self):
        """Check clearning a stack sizes the list correctly and preserves
        the other stack"""
        ts = TwoStack()
        for i in range(8):
            ts.push1(i)
        ts.push2(9)
        ts.clear1()

        self.assertEqual(2, ts.capacity(), 
            "After 9 pushes (8 stack1 1 stack2) and a clear" + \
                "of stack 1 capacity should  be 2")
        self.assertEqual(9,ts.top2(), "Top of stack 2 should be a 9")

    @weight(1)
    @number("1.8")
    def test_08(self):
        """Check clearning a stack sizes the list correctly and preserves
        the other stack"""
        ts = TwoStack()
        for i in range(8):
            ts.push2(i)
        ts.push1(8)
        ts.push1(9)

        self.assertEqual(16, ts.capacity(), 
            "After 10 pushes (8 stack2 and 2 stack1) " + \
                "stack 1 capacity should  be 16")
        
        ts.clear1()

        self.assertEqual(8, ts.capacity(), 
            "After 9 pushes (8 stack1 2 stack2) and a clear" + \
                "of stack 1 capacity should  be 8")
        self.assertEqual(7,ts.top2(), "Top of stack 2 should be a 7")

    @weight(1)
    @number("1.9")
    def test_09(self):
        """Large sets of pushes and pops from each stack"""
        ts = TwoStack()
        for i in reversed(range(1,21)):
            ts.push1(i)
        answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        ts_answer = []
        for _ in range(20):
            ts_answer.append(ts.pop1())

        self.assertEqual(answer_list, ts_answer, 
            "After 20 pushes and pops to stack 1")
        self.assertEqual(2, ts.capacity(), 
            "Capacity should be 2 after 20 pushes and pops")    

    @weight(2)
    @number("1.10")
    def test_10(self):
        """Large sets of pushes and pops from each stack"""
        ts = TwoStack()
        for i in range(1,21):
            ts.push1(i)
        stack1_poplist = []
        stack2_poplist = []

        for i in range(101,121):
            ts.push2(i)
        
        # pop alternating ones from stack1 and stack2
        for i in range(5):
            stack1_poplist.append(ts.pop1())
            stack2_poplist.append(ts.pop2())
        self.assertEqual([20, 19, 18, 17, 16], stack1_poplist, 
            "After 20 pushes and this should be the 5 pops")
        self.assertEqual([120, 119, 118, 117, 116], stack2_poplist, 
            "After 20 pushes to stack 2 this should be the 5 pops")
        
        self.assertEqual(32, ts.capacity(), 
            "After 40 pushes and 10 pops, stack capacity should be 32")

        # keep capacity at 32 by popping from stack 1 and adding to stack 2
        for i in range(10):
            stack2_poplist.append(ts.push2(116+i))
            ts.pop1()
            self.assertEqual(32, ts.capacity(), 
                "push/pop combos should keep the stack capacity at 32")

        ts.clear2()
        self.assertEqual(8, ts.capacity(), 
            "after clear2 capacity should be 8")
        ts.push2("Kevin")
        for i in range(5):
            self.assertEqual(5-i, ts.pop1(), "Popping from stack1 error")
     
        self.assertEqual(2, ts.capacity())
        self.assertEqual("Kevin", ts.top2(), "only this element should be on stack2")
        
    @weight(2)
    @number("1.11")
    def test_11(self):
        """Test of exceptions for stack underflow"""
        ts = TwoStack()
        failed = True
        try:
            ts.pop1()
            failed = False
        except:
            pass # throwing an exception is the expected result

        self.assertTrue(failed,"pop of an empty stack1 should" +
            " throw an exception")

        try:
            ts.pop2()
            failed = False
        except:
            pass # throwing an exception is the expected result

        self.assertTrue(failed,"pop of an empty stack2 should" +
             " throw an exception")
    

        try:
            ts.top1()
            failed = False
        except:
            pass # throwing an exception is the expected result

        self.assertTrue(failed,"top of an empty stack1 should" +
            " throw an exception")

        try:
            ts.top2()
            failed = False
        except:
            pass # throwing an exception is the expected result
        self.assertTrue(failed, "top of an empty stack2 should" +
            " throw an exception")

        ## push something on stack1 and make sure stack2 still throws

        ts.push1("Kevin")
        try:
            ts.pop2()
            failed = False
        except:
            pass # throwing an exception is the expected result
        self.assertTrue(failed,"pop of an empty stack2 should" +
             " throw an exception")

        try:
            ts.top2()
            failed = False
        except:
            pass # throwing an exception is the expected result

        self.assertTrue(failed,"top of an empty stack2 should" +
            " throw an exception")

        ts.pop1()
        ts.push2("Penny")

        try:
            ts.pop1()
            failed = False
        except:
            pass # throwing an exception is the expected result

        self.assertTrue(failed,"pop of an empty stack1 should" +
            " throw an exception")

        try:
            ts.top1()
            failed = False
        except:
            pass # throwing an exception is the expected result

        self.assertTrue(failed,"top of an empty stack2 should" +
            " throw an exception")

if __name__ == "__main__":
    unittest.main()
    
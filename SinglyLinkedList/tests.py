import unittest
import time
import timeout_decorator
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase): 
    sll = None
    TIMEOUT = 200
    
    @timeout_decorator.timeout(TIMEOUT)
    def setUp(self): 
        self.sll = SinglyLinkedList()

    @timeout_decorator.timeout(TIMEOUT)
    def test_init(self): 
        self.assertIsNone(self.sll.head.getData())
        self.assertEqual(self.sll.length, 0, "Initial length should be zero")
        
    @timeout_decorator.timeout(TIMEOUT)
    def test_addAtIndex(self):
        self.assertEqual(self.sll.size(), 0)
        self.assertIsNotNone(self.sll.head)

        self.sll.addAtIndex(0, "0a")
        self.sll.addAtIndex(1, "1a")
        self.sll.addAtIndex(2, "2a")
        self.sll.addAtIndex(3, "3a")
        self.sll.addAtIndex(2, "7a")
        self.assertEqual(self.sll.size(), 5)

        with self.assertRaises(IndexError) as context: 
            self.sll.addAtIndex(-22, "2a")

        with self.assertRaises(ValueError) as context: 
            self.sll.addAtIndex(2, None)

        curr = self.sll.getHead()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "0a")
    
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "1a")
        
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "7a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "2a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "3a")

    @timeout_decorator.timeout(TIMEOUT)
    def testAddToFront(self): 
        self.assertEqual(self.sll.size(), 0)
        
        self.sll.addToFront("1a")
        self.sll.addToFront("2a")
        self.sll.addToFront("3a")
        self.sll.addToFront("4a")
        self.sll.addToFront("5a")
        
        self.assertEqual(self.sll.size(), 5)

        curr = self.sll.getHead()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "5a")
    
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "4a")
        
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "3a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "2a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "1a")
        
    @timeout_decorator.timeout(TIMEOUT)
    def testAddToBack(self): 
        self.assertEqual(self.sll.size(), 0)

        self.sll.addToBack("0a")
        self.sll.addToBack("1a")
        self.sll.addToBack("2a")
        self.sll.addToBack("3a")
        self.sll.addToBack("4a")
        self.sll.addToBack("5a")
        
        self.assertEqual(self.sll.size(), 6)

        curr = self.sll.getHead()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "0a")
    
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "1a")
        
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "2a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "3a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "4a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "5a")

    @timeout_decorator.timeout(TIMEOUT)
    def testRemoveAtIndex(self): 
        self.assertEqual(self.sll.size(), 0)
        
        self.sll.addAtIndex(0, "0a")
        self.sll.addAtIndex(1, "1a")
        self.sll.addAtIndex(2, "2a")
        self.sll.addAtIndex(3, "3a")
        self.sll.addAtIndex(4, "4a")
        self.sll.addAtIndex(5, "5a")

        self.assertEqual(self.sll.size(), 6)
        
        self.assertEqual(self.sll.removeAtIndex(2), "2a")
        self.assertEqual(self.sll.size(), 5) 

        curr = self.sll.getHead()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "0a")
    
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "1a")
        
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "3a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "4a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "5a")

    @timeout_decorator.timeout(TIMEOUT)        
    def testRemoveFromFront(self): 
        self.assertEqual(self.sll.size(), 0)

        self.sll.addAtIndex(0, "0a")
        self.sll.addAtIndex(1, "1a")
        self.sll.addAtIndex(2, "2a")
        self.sll.addAtIndex(3, "3a")
        self.sll.addAtIndex(4, "4a")
        self.sll.addAtIndex(5, "5a")

        self.assertEqual(self.sll.size(), 6)
        
        self.assertEqual(self.sll.removeFromFront(), "0a")
        self.assertEqual(self.sll.size(), 5)

        curr = self.sll.getHead()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "1a")
    
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "2a")
        
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "3a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "4a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "5a")

    @timeout_decorator.timeout(TIMEOUT)        
    def testRemoveFromBack(self): 
        self.assertEqual(self.sll.size(), 0)

        self.sll.addAtIndex(0, "0a")
        self.sll.addAtIndex(1, "1a")
        self.sll.addAtIndex(2, "2a")
        self.sll.addAtIndex(3, "3a")
        self.sll.addAtIndex(4, "4a")
        self.sll.addAtIndex(5, "5a")

        self.assertEqual(self.sll.size(), 6)
        
        self.assertEqual(self.sll.removeFromBack(), "5a")
        self.assertEqual(self.sll.size(), 5)

        curr = self.sll.getHead()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "0a")
    
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "1a")
        
        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "2a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "3a")

        curr = curr.getNext()
        self.assertIsNotNone(curr)
        self.assertEqual(curr.getData(), "4a")

    @timeout_decorator.timeout(TIMEOUT)
    def testGet(self): 
        self.assertEqual(self.sll.size(), 0)

        self.sll.addAtIndex(0, "0a")
        self.sll.addAtIndex(1, "1a")
        self.sll.addAtIndex(2, "2a")
        self.sll.addAtIndex(3, "3a")
        self.sll.addAtIndex(4, "4a")
        self.sll.addAtIndex(5, "5a")

        self.assertEqual(self.sll.size(), 6)

        self.assertEqual(self.sll.get(0), "0a")
        self.assertEqual(self.sll.get(1), "1a")
        self.assertEqual(self.sll.get(2), "2a")
        self.assertEqual(self.sll.get(3), "3a")
        self.assertEqual(self.sll.get(4), "4a")
        self.assertEqual(self.sll.get(5), "5a")

    @timeout_decorator.timeout(TIMEOUT)
    def testToList(self): 
        expectedItems = [None] * 10

        for i in range(len(expectedItems)): 
            expectedItems[i] = "a" + str(i)
            self.sll.addToBack(expectedItems[i])
    
        arr = self.sll.toList()
        self.assertEqual(arr, expectedItems)

    @timeout_decorator.timeout(TIMEOUT)
    def testClearAndIsEmpty(self): 
        self.assertEqual(self.sll.size(), 0)

        self.sll.addAtIndex(0, "0a")
        self.sll.addAtIndex(1, "1a")
        self.sll.addAtIndex(2, "2a")
        self.sll.addAtIndex(3, "3a")
        self.sll.addAtIndex(4, "4a")
        self.sll.addAtIndex(5, "5a")

        self.assertEqual(self.sll.size(), 6)
        self.assertFalse(self.sll.isEmpty())

        self.sll.clear()
        self.assertEqual(self.sll.size(), 0)
        self.assertEqual(self.sll.getHead(), None)
        self.assertTrue(self.sll.isEmpty())

if __name__ == "__main__": 
    unittest.main() 

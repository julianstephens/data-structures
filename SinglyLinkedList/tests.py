import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase): 
    sll = None

    def setUp(self): 
        self.sll = SinglyLinkedList()

    # def test_init(self): 
    #     self.assertEqual(self.sll.head, None, "Initial head should be None")
    #     self.assertEqual(len(self.sll), 0, "Initial length should be zero")
    #     self.assertEqual(self.sll.length, 0, "Initial length should be zero")
        
    def test_insert(self):
        self.assertEqual(self.sll.size(), 0)
        self.assertIsNotNone(self.sll.head)

        self.sll.insert(0, "0a")
        self.sll.insert(1, "1a")
        self.sll.insert(2, "2a")
        self.sll.insert(3, "3a")
        self.sll.insert(2, "7a")
        # self.sll.insert(-22, "2a")
        self.assertEqual(self.sll.size(), 5)

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

    def testAddToFront(): 
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
        

    def testAddToBack(): 
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


if __name__ == "__main__": 
    unittest.main() 

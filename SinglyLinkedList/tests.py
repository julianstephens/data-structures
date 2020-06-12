import unittest
import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase): 
    sll = None

    def setUp(self): 
        self.sll = SinglyLinkedList()

    def test_init(self): 
        self.assertEqual(self.sll.head, None, "Initial head should be None")
        self.assertEqual(len(self.sll), 0, "Initial length should be zero")
        
    def test_insert(self): 
        self.assertEqual(self.sll.insert(0, "Timmy"),  )

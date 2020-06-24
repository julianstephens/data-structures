import unittest
import time
import timeout_decorator
from stack import Stack

class TestStack(unittest.TestCase): 
    stack = None
    TIMEOUT = 200

    @timeout_decorator.timeout(TIMEOUT)
    def setUp(self): 
        self.stack = Stack()

    @timeout_decorator.timeout(TIMEOUT)
    def test_init(self): 
        self.assertEqual(self.stack.getSize(), 0)

    @timeout_decorator.timeout(TIMEOUT)
    def test_push(self): 
        self.assertEqual(self.stack.getSize(), 0)

        self.stack.push(34)
        self.stack.push(29)
        self.stack.push(48)
        self.stack.push(59)

        with self.assertRaises(ValueError) as context: 
            self.stack.push(None)
        
        self.assertEqual(self.stack.getSize(), 4)
        
        expected = [34, 29, 48, 59]

        self.assertEqual(self.stack.toList(), expected) 

    @timeout_decorator.timeout(TIMEOUT)
    def test_pop(self): 
        self.assertEqual(self.stack.getSize(), 0)

        with self.assertRaises(RuntimeError) as context: 
            self.stack.pop()
        
        self.stack.push(34)
        self.stack.push(29)
        self.stack.push(48)
        self.stack.push(59)
    
        self.assertEqual(self.stack.pop(), 59)
        self.assertEqual(self.stack.getSize(), 3)

        expected = [34, 29, 48]

        self.assertEqual(self.stack.toList(), expected) 
        
    @timeout_decorator.timeout(TIMEOUT)
    def test_peek(self): 
        self.assertEqual(self.stack.getSize(), 0)

        with self.assertRaises(RuntimeError) as context: 
            self.stack.peek()
        
        self.stack.push(34)
        self.stack.push(29)
        self.stack.push(48)
        self.stack.push(59)
    
        self.assertEqual(self.stack.peek(), 59)
        self.assertEqual(self.stack.getSize(), 4)


if __name__ == "__main__": 
    unittest.main() 
 

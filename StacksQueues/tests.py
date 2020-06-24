import unittest
import time
import timeout_decorator
from stack import Stack
from queue import Queue

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


class TestQueue(unittest.TestCase): 
    queue = None
    TIMEOUT = 200

    @timeout_decorator.timeout(TIMEOUT)
    def setUp(self): 
        self.queue = Queue()

    @timeout_decorator.timeout(TIMEOUT)
    def test_init(self): 
        self.assertEqual(self.queue.getSize(), 0)

    @timeout_decorator.timeout(TIMEOUT)
    def test_enqueue(self): 
        self.assertEqual(self.queue.getSize(), 0)
        
        self.queue.enqueue(34)
        self.queue.enqueue(29)
        self.queue.enqueue(48)
        self.queue.enqueue(59)

        with self.assertRaises(ValueError) as context: 
            self.queue.enqueue(None)
        
        self.assertEqual(self.queue.getSize(), 4)
        
        expected = [34, 29, 48, 59]

        self.assertEqual(self.queue.toList(), expected) 

    @timeout_decorator.timeout(TIMEOUT)
    def test_dequeue(self): 
        self.assertEqual(self.queue.getSize(), 0)

        self.queue.enqueue(34)
        self.queue.enqueue(29)
        self.queue.enqueue(48)
        self.queue.enqueue(59)

        self.assertEqual(self.queue.dequeue(), 34)
        self.assertEqual(self.queue.getSize(), 3)
        
        expected = [None, 29, 48, 59]

        self.assertEqual(self.queue.toList(), expected) 
        
    @timeout_decorator.timeout(TIMEOUT)
    def test_peek(self): 
        self.assertEqual(self.queue.getSize(), 0)

        self.queue.enqueue(34)
        self.queue.enqueue(29)
        self.queue.enqueue(48)
        self.queue.enqueue(59)

        self.assertEqual(self.queue.peek(), 34)
        self.assertEqual(self.queue.getSize(), 4)
        
        expected = [34, 29, 48, 59]

        self.assertEqual(self.queue.toList(), expected) 



if __name__ == "__main__": 
    unittest.main() 
 

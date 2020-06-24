class Queue:
    def __init__(self): 
       """Initializes a new queue
       """
       self.backingList = []
       self.size = 0
       self.front = 0

    def isEmpty(self):
        """Checks if backing list is empty

        Returns:
            bool: True for empty, False otherwise
        """
        return len(self.backingList) == 0 

    def checkData(self, data): 
        """Checks if data is null

        Args:
            data (int): Data to be checked

        Raises: 
            ValueError: If data is null
        """
        if data is None: 
            raise ValueError("Cannot insert null data.")

    def getSize(self): 
        """Returns the size of the queue

        O(1) all cases

        Returns:
            int: The queue size
        """
        return self.size

    def toList(self):
        """Returns the queue's backing list

        O(1) in all cases

        Return:
            list: The backing list for the queue
        """
        return self.backingList

    def enqueue(self, data): 
        """Adds given data to the queue

        O(1) for all cases

        Args:
            data (int): The data to be added
        """
        self.checkData(data)

        self.backingList.append(data)
        self.size += 1

    def dequeue(self): 
        """Removes the data at the top of the queue 

        O(1) in all cases

        Returns: 
            int: The element that is removed

        Raises: 
            RuntimeError: If the list is already empty
        """
        if self.isEmpty(): 
            raise RuntimeError("Cannot dequeue from an empty queue.")
        
        removed = self.peek()
        self.backingList.pop()
        self.size -= 1

        return removed

    def peek(self): 
        """Returns the data at the top of the queue without removing it

        O(1) in all cases

        Returns: 
            int: The last element
        """
        if self.isEmpty(): 
            raise RuntimeError("Cannot peek an empty queue.")

        return self.backingList[-1]


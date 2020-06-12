class SinglyLinkedList:
    class __Node: 
        def __init__(self, data, next=None): 
            """Initializes Node with data d and next pointer n

            Args:
                data (int): An integer payload
                next (Node, optional): The next node in the SinglyLinkedList
            """
            self.data = data
            self.next = next
        
        def __eq__(self, other): 
            """Defines equality comparison for two nodes

            Args:
                other (Node): The node to compare against
            """
            return self.data == other.data and self.next == other.next

        def getData(self): 
            """Gets a node's payload

            Returns: 
                The stored payload
            """
            return self.data

        def getNext(self): 
            """Gets a node's next reference

            Returns: 
                The current next reference
            """
            return self.next

        def setData(self, data): 
            """Sets the node's payload
            
            Args: 
                data (int): An integer payload
            """
            self.data = data

        def setNext(self, next):
            """Sets the node's next pointer

            Args:
                next (Node): The new next node
            """
            self.next = next
    
    def __init__(self, contents=[]): 
        """Initializes a new SinglyLinkedList

        Args:
            contents (list, optional): The contents of the new SinglyLinkedList
        """
        self.head = SinglyLinkedList.__Node(None, None)
        self.length = 0

        for item in contents: 
            self.append(item)

    def __checkIndex____(index): 
        """Checks that the index is in bounds

        Args:
            index (int): Index to check 

        Raises: 
            IndexError: If the index is out of bounds
        """
        if index < 0 or index >= self.length: 
            raise IndexError('Please specify an index that is not negative' 
                             + 'and/or greater than the size of the data structure.')
    
    def __checkData__(data): 
        """Checks that the data is not null

        Args:
            data (int): Data to check

        Raises: 
            ValueError: If data is null
        """
        if data is None: 
            raise ValueError('Cannot add null data to the data structure.')

    def __addToFront__(self, data): 
        """Adds a node to the front of the SinglyLinkedList

        Runs O(1) for alll cases

        Args:
            data (int): The data for the new node
        """
        self.__checkData__(data)

        if self.head is None: 
            newNode = SinglyLinkedList.__Node(data)
            self.head = newNode
            newNode.setNext(newNode)
        else: 
            newNode = SinglyLinkedList.__Node(self.head.getData())
            newNode.setNext(self.head.getNext())
            self.head.setNext(newNode)
            self.head.setData(data)

        self.length += 1

    def __addToBack__(self, data): 
        """Add a node to the back of the SinglyLinkedList

        O(1) for all cases

        Args:
            data (int): The data to be added
        """
        self.__checkData__(data)

        curr = self.head
        while curr.getNext() is not None: 
            curr = curr.getNext()

        newNode = SinglyLinkedList.__Node(data)
        curr.setNext(newNode)

        self.length += 1


    def insert(self, index, data): 
        """Add a node at the specified index

        O(1) for add to indices 0 and {@code self.length}

        Args:
            data (int): The data for the new node
        """
        self.__checkIndex__(index)
        self.__checkData__(data)

        if index == 0: 
            self.__addToFront__(data)        
        elif index == self.length:
            self.__addToBack__(data)
        else: 
            curr = self.head
            newNode = SinglyLinkedList.__Node(data)

            for i in range(index-1): 
                curr = curr.getNext()

            newNode.setNext(curr.getNext())
            curr.setNext(newNode) 
            self.length += 1

    def append(self, data): 
        """Add a node to the back of the SinglyLinkedList

        O(1) for all cases

        Args:
            data (int): The data for the new node
        """
        self.__checkData__(data)

        self.__addToBack__(data)

    def delete(self, index): 
        """Removes node at specified index

        O(1) for index 0, O(n) for all other cases

        Args:
            index (int): The index of the node to be removed
        """
        self.__checkIndex__(index)

        if self.length == 1: 
            self.head = None
        else:

            curr = self.head

            for node in range(index): 
                curr = curr.getNext()
        
            curr.setNext(curr.getNext.getNext())

        self.length -= 1

    def contains(self, data): 
        """Checks if node with specif

        Worst case O(n)

        Args:
            data (int): Data to search for

        Returns:
            Index of node if found or -1 if not found
        """
        self.__checkData__(data)

        curr = self.head
        index = 0

        while curr.getNext() is not None: 
            if curr.getData() == data: 
                return index
    
            curr = curr.getNext()
            index += 1

        return -1

    def get(self, index): 
        """Returns node at the specified index

        O(1) for index 0, O(n) for all other cases

        Args:
            index (int): The index of the requested element

        Returns: 
            The data at the specified index
        """
        self.__checkIndex__(index)

        if index == 0: 
            return self.head.getData()
        else: 
            curr = self.head

            for node in range(index): 
                curr = curr.getNext()

            return curr.getNext().getData()

    def toList(self): 
        """Converts the SinglyLinkedList into a list

        O(n) for all cases

        Returns: 
            List of length {@code self.length} holding all of the objects in
            the SinglyLinkedList in the same order

        """
        convertedList = [None] * self.length
        curr = self.head

        for i in range(self.length): 
            convertedList[i] = curr.getData()
            curr = curr.getNext()

        return convertedList
    
    def isEmpty(self):
        """Returns a booolean value indicating if the SinglyLinkedList is empty

        O(1) for all cases

        Returns:
            Bool True if empty; False otherwise
        """
        return self.head is None

    def clear(self): 
        """Clears the SinglyLinkedList of all data

        O(1) for all cases  
        """
        self.head = None
        self.length = 0

    def length(self): 
        """Returns the size of the SinglyLinkedList

        O(1) for all cases

        Returns: 
            Int {@code self.length}
        """
        return self.length

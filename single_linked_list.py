class SinglyLinkedList:
    class __Node: 
        def __init__(self, data, next=None): 
            self.data = data
            self.next = next
         
        def getData(self): 
            return self.data

        def getNext(self): 
            return self.next

        def setData(self, data): 
            self.data = data

        def setNext(self, next):
            self.next = next
    
    def __init__(self, contents=[]): 
        self.head = SinglyLinkedList.__Node(None, None)
        self.length = 0

        for item in contents: 
            self.append(item)

    def checkIndex(index): 
        if index < 0 or index >= self.length: 
            raise IndexError('Please specify an index that is not negative' 
                             + 'and/or greater than the size of the data structure.')
    
    def checkData(data): 
        if data is None: 
            raise ValueError('Cannot add null data to the data structure.')

    def __getNode__(self, index): 
        checkIndex(index)
        
        if index == 0: 
            return self.head.getData()
        else: 
            curr = self.head

            for i in range(0, index-1): 
                curr = curr.getNext()

            return curr.getNext().getData();

    def __setNode__(self, index, data): 
        checkIndex(index)
        checkData(data)

        if index == 0: 
            self.head.setData(data)
        else: 
            curr = self.head

            for i in range(0, index-1): 
                curr = curr.getNext()

            curr.getNext().setData(data);
        
        return data

    def __addToFront__(self, data): 
        checkData(data)

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
        checkData(data)

        curr = self.head
        while curr.getNext() is not None: 
            curr = curr.getNext()

        newNode = SinglyLinkedList.__Node(data)
        curr.setNext(newNode)

        self.length += 1


    def insert(self, index, data): 
        checkIndex(index)
        checkData(data)

        if index == 0: 
            self.__addToFront__(data)        
        elif index == self.length:
            self.__addToBack__(data)
        else: 
            curr = self.head
            newNode = SinglyLinkedList.__Node(data)

            for i in range(0, index-1): 
                curr = curr.getNext()

            newNode.setNext(curr.getNext())
            curr.setNext(newNode) 
            self.length += 1 


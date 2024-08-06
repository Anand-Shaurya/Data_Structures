class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(str(temp.value))
            temp = temp.next
        return ('->'.join(arr))

        
    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            temp.next = Node(value)

    
n = 5
arr = [1, 7, 9, 11, 45]

l1 = LinkedList() 
for i in arr:
    l1.insert(i)

print(l1)




        

             
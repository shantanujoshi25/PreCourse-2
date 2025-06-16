# // Time Complexity : O(n)
# // Space Complexity : O(1)

# Node class  
class Node: 
    
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None    
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        
  
    def push(self, new_data): 
        if(self.head is None):
            self.head = Node(new_data)       
        else:
            temp = Node(new_data) 
            temp.next = self.head 
            self.head = temp
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        middle_node = self.head
        end_node = self.head
        while(end_node.next is not None):
            if(end_node.next.next is not None):
                end_node = end_node.next.next
                middle_node = middle_node.next
            else:
                break
        print(middle_node.data)
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 

# // Time Complexity : O(n log n)  
# // Space Complexity : O(n)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# the approach is to use the pivot and sort all the 
# smaller values on left side and larger values on right
# further recursively call the function on left and right side of pivot

# Inside the partition function, use the last element as pivot,
# use li to track the lower values index, swap and keep lower values in this index.
# at last swap the pivot with last element on lower index

def partition(arr,low,high):
    pivot = high
    li = low
    for i in range(low,high):
        if(arr[i] <= arr[pivot]):
            
            temp = arr[i]
            arr[i] = arr[li]
            arr[li] = temp
            li+=1

    temp = arr[high]
    arr[high] = arr[li] 
    arr[li] = temp

    return li
  
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if(low<high):
        i = partition(arr,low,high)
        quickSort(arr,low,i-1)
        quickSort(arr,i+1,high)
    
    
    
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 

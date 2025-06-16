# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  pivot = high
  li = low
  for i in range(low,high):
      if(arr[i] <= arr[pivot]):
          
          temp = arr[i]
          arr[i] = arr[li]
          arr[li] = temp
          li+=1

  temp = arr[len(arr)-1]
  arr[len(arr)-1] = arr[li] 
  arr[li] = temp

  return li


def quickSortIterative(arr, l, h):
  stack = []
  stack.append((l, h))
  
  while stack:  
    low, high = stack.pop()  
        
    if low < high:
        i = partition(arr, low, high)
        stack.append((low, i - 1))     
        stack.append((i + 1, high))
        

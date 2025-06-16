# // Time Complexity : O(nlogn)
# // Space Complexity : O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  if(len(arr) <= 1):
    return arr
  mid = len(arr) // 2
  
  l_arr = arr[:mid]
  r_arr = arr[mid:]
  
  mergeSort(l_arr)   
  mergeSort(r_arr) 
  merge(arr, l_arr, r_arr)
  
def merge(arr, l_arr,r_arr):
  sorted_arr = []
  i=0
  j=0
  k=0
  
  while i < len(l_arr) and j < len(r_arr):
    if l_arr[i] <= r_arr[j]:
        arr[k] = l_arr[i]  
        i += 1
    else:
        arr[k] = r_arr[j]  
        j += 1
    k += 1
  
  while i < len(l_arr):
    arr[k] = l_arr[i]
    i += 1
    k += 1
     
  while j < len(r_arr):
    arr[k] = r_arr[j]
    j += 1
    k += 1

# Code to print the list 
def printList(arr): 
  print(arr)
  
  
# driver code to test the above code 
if __name__ == '__main__': 
  arr = [12, 11, 13, 5, 6, 7]  
  print ("Given array is", end="\n")  
  printList(arr) 
  mergeSort(arr) 
  print("Sorted array is: ", end="\n") 
  printList(arr) 

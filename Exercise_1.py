# // Time Complexity : O(log n)
# // Space Complexity : O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
 
  while(l<=r):
    m = ((l+r)//2)
    if(arr[m] == x):
      return m
    elif(arr[m] > x):
      r = m-1
    else:
      l = m+1
  return -1
    
  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")

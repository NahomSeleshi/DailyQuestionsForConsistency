#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        selectionSort(self, arr,len(arr))
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            curMin, curMinIndex = arr[i],i
            for j in range(i+1, len(arr)):
                if curMin > arr[j]:
                    curMin = arr[j]
                    curMinIndex = j
            arr[i], arr[curMinIndex] = arr[curMinIndex], arr[i]
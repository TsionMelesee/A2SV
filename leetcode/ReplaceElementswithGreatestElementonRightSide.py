class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = -1
        size = len(arr)-1
        for i in range(size, -1,-1):
            temp = arr[i]
            arr[i]= x
            x = max(x,temp)
        return arr
            
        

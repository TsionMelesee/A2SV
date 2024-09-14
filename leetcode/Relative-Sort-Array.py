class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        store = [0] * (max(arr1) + 1)
        for i in arr1:
            store[i] += 1

        result = []
        for num in arr2:
            result.extend([num] * store[num])
            store[num] = 0
        
        for index in range(len(store)):
            if store[index] > 0:
                result.extend([index] * store[index])

        return result

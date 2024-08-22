class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        array = []
        
        for number in nums1:
            if number not in dic:
                dic[number] = 1
            else:
                dic[number] += 1
        
        for number in nums2:
            if number in dic and dic[number] > 0:
                array.append(number)
                dic[number] -= 1
        
        return array

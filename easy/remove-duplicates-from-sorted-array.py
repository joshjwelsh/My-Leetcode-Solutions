class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap = dict()
        deleteVals = list()
        for element in nums:
            if element not in hashMap:
                hashMap[element] = 1
            else:
                hashMap[element] += 1
                deleteVals.append(element)
                
        for val in deleteVals:
            nums.remove(val)
        return len(nums)
                
                
            

class Solution:
    def slidingWindow(self, index, s):
        hashMap = dict()
        myList = []
        for i in range(index, len(s)):
            letter = s[i]
            if letter in hashMap:
                return myList
            else:
                hashMap[letter] = 1
                if letter is not None:
                    myList.append(letter)
        return myList
    
    def findLongest(self, array):
        if len(array) == 1:
            return len(array[0])

        else:
            print(array)
            mx = len(array[0])
            for element in array:
                if mx < len(element):
                    mx = len(element)
            return mx
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            solutions = list()
            sol = Solution()
            for i in range(len(s)):
                noneTest = sol.slidingWindow(i, s)
                if noneTest is not None:
                    solutions.append(sol.slidingWindow(i, s))
            return sol.findLongest(solutions)
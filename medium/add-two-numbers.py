# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def tranverse(self, ln):
        myList = []
        while(ln):
            myList.append(ln.val)
            ln = ln.next
        return myList
    
    def getLastNode(self, node):
        while node.next is not None:
            node = node.next
        return node
    
    def packList(self, result):
        head = ListNode(result[0])
        tail = head
        for val in result[1:]:
            node = ListNode(val)
            tail.next = node 
            tail = tail.next
            
        return head
    
    def listAdder(self, l1, l2):
        if len(l1) > len(l2):
            newList = l1 
            for i,val in enumerate(l2):
                newList[i] += val
        elif len(l2) >= len(l1):
            newList = l2
            for i,val in enumerate(l1):
                newList[i] += val
        return newList
              
    def overflowHandler(self, result):
        for i,val in enumerate(result):
            if val >= 10:
                rem = 1
                val = val % 10 
                if i+1 < len(result):
                    result[i+1] += 1
                else:
                    result = result + [0]
                    result[i+1] += 1
                    
                result[i] = val 
        return result
     
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sol = Solution()
        list1 = sol.tranverse(l1)
        list2 = sol.tranverse(l2)
        result = sol.listAdder(list1,list2)
        overflow = sol.overflowHandler(result)
        # print(overflow)
        node = sol.packList(overflow)
        # print(node)
        return node
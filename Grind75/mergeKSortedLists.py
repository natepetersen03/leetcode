# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        returnList = head
        size = 0
        while len(lists) > 0:
            minIndex = None
            minimum = ListNode(10001)
            a = 0
            while a < len(lists):
                curr = lists[a]
                #covering the case where a null node is in the list
                if curr == None:
                    lists.pop(a)
                    a -= 1
                else:
                    # if min is found
                    if curr.val < minimum.val:
                        # update min
                        minimum = curr
                        minIndex = a
                        # check if this node.next is null
                a += 1
            # no nimimum found (empty list)
            if minIndex == None:
                break
            # if this is the first node to be added, initialize the head
            if size == 0:
                head = ListNode(minimum.val)
                returnList = head
            # otherwise add the node to the end of the list
            else:
                returnList.next = ListNode(minimum.val)
                returnList = returnList.next
            size += 1
            lists[minIndex] = lists[minIndex].next
        #return the head of the sorted list
        return head
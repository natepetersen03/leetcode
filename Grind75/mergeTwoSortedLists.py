# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # whichever is less you add
        head = None
        l = None
        #merge with two non-null lists, comparison necessary
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                if head == None:
                    head = ListNode(list1.val)
                    l = head
                else:
                    l.next = ListNode(list1.val)
                    l = l.next
                list1 = list1.next
            else:
                if head == None:
                    head = ListNode(list2.val)
                    l = head
                else:
                    l.next = ListNode(list2.val)
                    l = l.next
                list2 = list2.next
        #list1 non-null, list2 null
        while list1 != None:
            if head == None:
                head = ListNode(list1.val)
                l = head
            else:
                l.next = ListNode(list1.val)
                l = l.next
            list1 = list1.next
        #list2 non-null, list1 null
        while list2 != None:
            if head == None:
                head = ListNode(list2.val)
                l = head
            else:
                l.next = ListNode(list2.val)
                l = l.next
            list2 = list2.next
        return head
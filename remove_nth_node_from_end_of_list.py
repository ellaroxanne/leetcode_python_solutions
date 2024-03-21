class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            head = None
            return head
        my_node = head
        parent_node = None
        sz = 1
        while my_node.next != None:
            sz += 1
            my_node = my_node.next
        n = sz - n + 1
        count = 1
        my_node_2 = head
        while count != n:
            count += 1
            parent_node = my_node_2
            my_node_2 = my_node_2.next
        if parent_node == None:
            head = my_node_2.next
            return head
        parent_node.next = my_node_2.next
        return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(2)
current = list1

current.next = ListNode(3)

print(list1.val)
print(list1.next.val)
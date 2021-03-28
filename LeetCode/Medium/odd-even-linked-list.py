# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: # if listNode is empty or contains only one element
            return head
        odd = head
        even_pointer = head.next  # pointer to even indices starts after the head
        even_list = even_pointer # even_list is just a pointer to the start of the even list head
        # print(f"odd.val:{odd.val}")
        # print(f"even_pointer.val:{even_pointer.val}")
        while even_pointer and even_pointer.next:
            odd.next = even_pointer.next
            odd = odd.next
            even_pointer.next = odd.next
            even_pointer = even_pointer.next
            print(f"odd.val:{odd.val}")

        odd.next = even_list
        return head


if __name__ == "__main__":
    solution = Solution()
    # [1,2,3,4,5]
    listNode = ListNode(5)
    listNode2 = ListNode(4, listNode)
    listNode3 = ListNode(3, listNode2)
    listNode4 = ListNode(2, listNode3)
    listNode5 = ListNode(1, listNode4)

    solution.oddEvenList(listNode5)

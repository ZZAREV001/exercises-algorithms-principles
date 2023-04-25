# Remove K-th last element from linked list
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):  # print the value of the linked list data structure
        n = self
        answer = ''
        while n:
            answer += str(n.val)
            n = n.next
        return answer


def remove_kth_from_linked_list(node, k):
    slow, fast = node, node
    for i in range(k):
        fast = fast.next
    if not fast:
        return node.next

    # advance and find both k-th element. At the end of the while loop we find the k-th element.
    prev = None
    while fast:
        prev = slow
        fast = fast.next
        slow = slow.next
    prev.next = slow.next
    return node


head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
remove_kth_from_linked_list(head, 3)
print(head)

remove_kth_from_linked_list(head, 3)
print(head)

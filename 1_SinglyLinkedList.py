#1. singly linked list

class ListNode:
    def __init__(self, value = 0, next = None ):
        self.value = value
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next, prev, current = prev, current, next_temp
    return prev

def printlist(head): 
    print( " " )   
    while head:
        print(f"{head.value}", end = " ")
        head = head.next


printlist(node1)  #друкуємо список
reverse_list(node1) #робимо реверс
printlist(node3) #друкуємо реверсний список

def merge_sort(head):
    if not head or not head.next:
        return head

    # Розділяємо список на дві частини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивно сортуємо дві половини
    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Злиття двох відсортованих половин
    sorted_list = merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.value <= right.value:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    return result

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next


# Створимо новий список, що не є впорядкованим.

node11 = ListNode(4)
node22 = ListNode(2)
node33 = ListNode(5)
node44 = ListNode(1)
node55 = ListNode(3)

node11.next = node22
node22.next = node33
node33.next = node44
node44.next = node55

#впорядкуємо
printlist(node11)
sorted_head = merge_sort(node11)
printlist(sorted_head)

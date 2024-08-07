from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h = ListNode(1000)
g = ListNode(999, h)
j = ListNode(500, g)

i = ListNode(74)
c = ListNode(9, i)
b = ListNode(-9, c)
a = ListNode(-13, b)

k = ListNode(243)
f = ListNode(100, k)
e = ListNode(99, f)
d = ListNode(10, e)

l = ListNode()
m = ListNode()

# so the linked lists are l, m, a, d and j.

def mergelist(list1: Optional[ListNode], list2: Optional[ListNode]):
    temp = ListNode()
    if not list1:
        return list2
    elif not list2:
        return list1
    else:
        i = list1
        j = list2
        while i != None and j != None: 
            if i.val <= j.val:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next

        if i != None:
            temp.next = i
        elif j != None:
            temp.next = j
    
    return temp

x = mergelist(l, j)
y = mergelist(l, m)
z = mergelist(a, d)
xy = mergelist(a, j)
xz = mergelist(d, j)

while x != None:
    print(x.val)
    x = x.next
print()

while y != None:
    print(y.val)
    y = y.next
print()

while z != None:
    print(z.val)
    z = z.next
print()

while xy != None:
    print(xy.val)
    xy = xy.next
print()

while xz != None:
    print(xz.val)
    xz = xz.next
print()
m, n = list(map(int, input().split()))


class Node:
    def __init__(self, next, val):
        self.val = val
        self.next = next
        return

    def __repr__(self) -> str:
        return f"{self.val}->{repr(self.next)}"


head = Node(None, 1)
tail = Node(None, "tail")

p = head
for i in range(2, n):
    p.next = Node(None, i)
    p = p.next

counter = 0
lucky_dog = head.next  # 这个计算过程有个坑，第一个模数2不是第一个幸运数的值，而此后都是对应幸运数的值
while lucky_dog:
    if lucky_dog.val > m:
        counter += 1

    p = head
    a = lucky_dog.val - 1  # a就是此时p对应的周期标号
    while p is not None:
        if a == 1:  # 因为只能删除p后面的结点，所以要在a为1时删除
            if p.next is None:
                break  # 我觉得可能不存在一种能省略这里的检查的写法
            p.next = p.next.next
            p = p.next
            a = lucky_dog.val - 1
        else:
            p = p.next
            a -= 1
    lucky_dog = lucky_dog.next  # 这里阴差阳错地对了

if m < 2:
    counter -= 1
print(counter)

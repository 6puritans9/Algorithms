import sys


def get_input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.length = 0

    def push(self, instruction, num):
        new_node = Node(num)

        if not self.length:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.head
            self.length += 1
            return

        if instruction == "push_front":
            ex_head = self.head.next

            new_node.next = ex_head
            ex_head.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            self.length += 1

        elif instruction == "push_back":
            ex_tail = self.tail.prev

            new_node.prev = ex_tail
            ex_tail.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            self.length += 1

    def pop(self, instruction):
        if not self.length:
            return -1

        if instruction == "pop_front":
            ex_head = self.head.next

            self.head.next = ex_head.next
            self.head.next.prev = self.head
            self.length -= 1
            return ex_head.value

        elif instruction == "pop_back":
            ex_tail = self.tail.prev

            self.tail.prev = ex_tail.prev
            self.tail.prev.next = self.tail
            self.length -= 1
            return ex_tail.value

    def size(self):
        return self.length

    def empty(self):
        if self.length:
            return 0
        return 1

    def front(self):
        if not self.length:
            return -1
        return self.head.next.value

    def back(self):
        if not self.size():
            return -1
        return self.tail.prev.value


if __name__ == "__main__":
    deque = Deque()

    N = int(get_input())
    for _ in range(N):
        user_input = get_input().split()
        if len(user_input) > 1:
            instruction, num = user_input
            deque.push(instruction, int(num))
        else:
            user_input = user_input[0]
            if user_input == "front":
                print(deque.front())
            elif user_input == "back":
                print(deque.back())
            elif user_input == "size":
                print(deque.size())
            elif user_input == "empty":
                print(deque.empty())
            elif user_input == "pop_front":
                print(deque.pop(user_input))
            elif user_input == "pop_back":
                print(deque.pop(user_input))

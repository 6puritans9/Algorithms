import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def traverse(in_start, in_end, post_start, post_end) -> None:
    global index_map

    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    root_idx = index_map[root]
    subtree_size = root_idx - in_start

    print(root, end=" ")
    traverse(in_start, root_idx - 1, post_start, post_start + subtree_size - 1)  # left subtree
    traverse(root_idx + 1, in_end, post_start + subtree_size, post_end - 1)  # right subtree



if __name__ == "__main__":
    # 1. There is a binary tree that has N nodes.
    # 2. There are no duplicate nodes, and the number is in ascending order.
    # 3. When its in-order and post-order are given,
    # 4. Find the pre-order.

    # Constraints
    # TIME 5000ms
    # SPACE 128MB
    # 1. 1 <= N <= 10^5

    # Approach
    # 1. Binary tree can be reconstructed with a hash map.
    # 2. From root, each node can have L, R.
    # 3. The last element of post-order is root.

    # 4. Find the index of the root node in the in-order array,
    #       L: idx-1 element, R: idx+1 element.
    # 6. Fill the left and right tree recursively.

    n = int(input())
    in_order = tuple(int(num) for num in input().split())
    post_order = tuple(int(num) for num in input().split())

    index_map = {num: idx for idx, num in enumerate(in_order)}
    traverse(0, n - 1, 0, n - 1)

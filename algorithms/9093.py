import sys


def get_input():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    T = int(get_input())
    sentences = []
    for _ in range(T):
        sentences.append( get_input().split())
    for sentence in sentences:
        for word in sentence:
            print(f"{word[::-1]}", end=" ")
        print()

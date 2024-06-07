import sys

input = sys.stdin.readline
print = sys.stdout.write


if __name__ == "__main__":
    N = int(input())
    words = []

    for i in range(N):
        words.append(([syl for syl in input().rstrip().split()]))

    for word in words:
        word[0] = "god"
        for syllable in word:
            print(f"{syllable}")
        print("\n")

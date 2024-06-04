import sys
print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    word = get_input()
    suffix = []

    for i in range(len(word)):
        substring = word[i::]
        if substring not in suffix:
            suffix.append(substring)

    for element in sorted(suffix):
        print(f"{element}\n")

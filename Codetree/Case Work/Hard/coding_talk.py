def find_did_not_read(n: int, m: int, p: int, messages: list[tuple[str, int]]) -> list[str]:
    # TC = O(NM)
    # SC = O(M)

    target_unread_count = int(messages[p - 1][1])
    if not target_unread_count:
        return []

    people_in_chat = [chr(ord('A') + i) for i in range(n)]
    unread_people = []

    for person in people_in_chat:
        for sender, unread_count in messages:
            if sender == person and unread_count >= target_unread_count:  # Read the message
                break
        else:
            unread_people.append(person)

    return unread_people


if __name__ == "__main__":
    # N peoples are in a chat.
    # Each one has name from 'A' to 'A + N'.
    # M for the number of messages, p for the order of the message that needs to be read.
    # For given M messages (sender, count(people did not see)),
    # find out those people who might not read the messages.

    # Constraints
    # TIME 5000ms
    # SPACE 288MiB
    # 1 <= N <= 26
    # 1 <= p <= M <= 10^2
    # 0 <= u <= N-1

    # Approach
    # This one didn't go as I expected in the first sight.
    # The basic premise for this problem is that,
    # if two messages by different senders had same unread_count,
    # those two senders have read each other's message.
    # Because, if someone else read message, those two unread count will differ.
    # Understanding this flow is the key of this problem.

    # 1. For the specific message p,
    #   people who send messages after p are considered to read p
    # 2. For each person in the chat,
    #   if a person sent a message, and its unread_count is same as p's,
    #   they have read each other's message
    # 3. So, the logic goes
    #       iterating over people:
    #           for sender, unread_count in messages:
    #               if unread_count < p_unread_count:
    #                   someone else read that message, cannot guarantee the sender read p
    #               else:
    #                   no one else have read that message, can guarantee the sender read p
    # 4. If p's unread_count is 0, all the people have read that.

    n, m, p = map(int, input().split())
    messages = []
    for _ in range(m):
        sender, unread_count = input().split()
        messages.append((sender, int(unread_count)))

    result = find_did_not_read(n, m, p, messages)
    print(" ".join(result))

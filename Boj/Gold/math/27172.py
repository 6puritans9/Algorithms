import sys

input = sys.stdin.readline


def result_after_game(n: int, cards: tuple[int, ...]) -> list[int]:
    # TC = O(N + N*log(max_card)) = O(Nlog(max_card) == O(10^5 * 6log10) = O(10^5)
    # SC = O(N)

    scores = [0 for _ in range(n)]
    max_card = max(cards)
    card_idx_map = {card: idx for idx, card in enumerate(cards)}  # O(N)

    for i, card in enumerate(cards):  # O(N)
        multiple = card * 2
        while multiple <= max_card:  # O(log(max_card))
            if multiple in card_idx_map:
                scores[i] += 1
                scores[card_idx_map[multiple]] -= 1
            multiple += card

    return scores


if __name__ == "__main__":
    # 1. This is a number dividing game.
    # 2. The rules are as below:
    #       a. Before starting the game, a shuffled card is distributed to each player.
    #       b. For each turn, a player challenges the other players.
    #       c. If (opponent's card number) % (player's card number) == 0, the player wins.
    #           elif (player's card number) % (opponent's card number) == 0, the player loses.
    #           else, draw.
    #       d. Winner takes a point, loser loses a point. draw does nothing.
    #       e. The game ends after challenging every other player.
    # 3. When the numbers of each player has got are given,
    #       find the score of all players after the game.

    # Constraints
    # TIME 1000ms
    # SPACE 1024MB
    # 1. 2 <= N <= 10^5
    # 2. 1 <= card number <= 10^6
    # 3. Every number is distinct.

    # Approach
    # 1. The simplest solution will be a nested loop,
    #       which takes O(N^2) = O(10^12) > 1000ms.
    # 2. This should take O(N) to meet the time limit though.
    # 3. The key is bidirectional computation for each challenge.
    # 4. Create an N sized result array,
    #       which represents the scores of each player to each cell.
    # 5. As the smallest multiple of each number starts from (number*2),
    #       the calculation should range from (number*2) to max_card.
    # 6. while multiple <= max_card:
    #       if multiple in cards:
    #           result[card] += 1
    #           result[multiple] -= 1
    #       multiple += card
    # 7. return the result

    n = int(input())
    cards = tuple(int(num) for num in input().split())
    result = result_after_game(n, cards)
    print(" ".join(map(str, result)))

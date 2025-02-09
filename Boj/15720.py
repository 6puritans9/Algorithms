def get_new_price(items, amount):
    DISCOUNT = 0.9
    sum = 0

    for idx, price in enumerate(items):
        if idx <= amount - 1:
            sum += price * DISCOUNT
            continue
        sum += price

    return sum


if __name__ == "__main__":
    burgers, sides, beverages = [int(num) for num in input().split()]
    burgers_prices = [int(num) for num in input().split()]
    burgers_prices.sort(reverse=True)
    sides_prices = [int(num) for num in input().split()]
    sides_prices.sort(reverse=True)
    beverages_prices = [int(num) for num in input().split()]
    beverages_prices.sort(reverse=True)

    regular_sum = 0
    eligible_amount = min(burgers, sides, beverages)
    event_sum = 0

    regular_sum = sum(burgers_prices) + sum(sides_prices) + sum(beverages_prices)
    event_sum = get_new_price(burgers_prices, eligible_amount) + get_new_price(sides_prices,
                                                                               eligible_amount) + get_new_price(
        beverages_prices, eligible_amount)

    print(regular_sum)
    print(int(event_sum))

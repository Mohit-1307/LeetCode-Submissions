class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        bars = 0

        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue

            can_buy = min(freq[price], coins // price)

            bars += can_buy
            coins -= can_buy * price

            if coins < price:
                continue

        return bars
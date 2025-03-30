class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        max_days = (n << 1) + 10
        secret_knowledge_counts = [0] * max_days
        current_day_counts = [0] * max_days
        current_day_counts[1] = 1
        for day in range(1, n + 1):
            if current_day_counts[day]:
                secret_knowledge_counts[day] += current_day_counts[day]
                secret_knowledge_counts[day + forget] -= current_day_counts[day]
                next_share_day = day + delay

                while next_share_day < day + forget:
                    current_day_counts[next_share_day] += current_day_counts[day]
                    next_share_day += 1
        modulo = 10 ** 9 + 7
        return sum(secret_knowledge_counts[: n + 1]) % modulo

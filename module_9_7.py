def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result < 2:
            return "Не является простым"

        for i in range(2, result // 2 + 1):
            if result % i == 0:
                return "Составное", result

        return "Простоe", result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


rrr = sum_three(1, 1, 77)
print(rrr)

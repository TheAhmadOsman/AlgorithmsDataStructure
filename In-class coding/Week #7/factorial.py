def fact_iter(n):
    fact_num = 1
    i = 1
    while i <= n:
        fact_num *= i
        i += 1
    return fact_num


def fact_rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact_rec(n-1)


def main():
    print(fact_iter(5))
    print(fact_rec(5))

main()

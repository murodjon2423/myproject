def f(n):
    result = n**5 + 8 * n**4 - 5 * n**3 + 3 * n**2 + n - 12
    return result


n = int(input("n ni kiriting (|n| ≤ 10): "))


result = f(n)


print(f"f({n}) = {result}")

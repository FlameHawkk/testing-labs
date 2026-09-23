def test(M, N):
    return N * N + M * (2 * N - 1)

TESTS = [
    (6, 6, 102),
    (3, 3, 24),
    (0, 5, 25),
    (5, 1, 6),
    (1, 1, 2),
    (0, 1, 1),
    (12, 4, 100)
]

print("=== Тесты ===")
print("M N -> result")
for M, N, exp in TESTS:
    got = test(M, N)
    print(M, N, "->", got, "OK" if got == exp else f"FAIL (нужно {exp})")

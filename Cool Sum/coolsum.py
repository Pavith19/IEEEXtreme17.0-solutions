"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""

MOD = 998244353

def binomial_coeff(n, k, mod):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    denom = 1
    for i in range(k):
        num = num * (n - i) % mod
        denom = denom * (i + 1) % mod
    return num * pow(denom, mod - 2, mod) % mod

def compute_sequence(k, n, t):
    results = []
    for i in range(n + 1):
        sum_val = 0
        for j in range(k + 1):
            binom = binomial_coeff(k, j, MOD)
            term = binom * pow(i, j, MOD) * pow(t, k - j, MOD) % MOD
            sum_val = (sum_val + term) % MOD
        results.append(sum_val)
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    k = int(data[0])
    n = int(data[1])
    t = 10  # Assuming t is a constant given in the example

    result = compute_sequence(k, n, t)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()


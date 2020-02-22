import math


def iter_gcd(x, y):
    mn = min(x, y)
    ans = 0
    for i in range(1, mn):
        if x % i == 0 and y % i == 0 and i > ans:
            ans = i
    return ans


def euclid_gcd(x, y):
    if y == 0:
        return x
    return euclid_gcd(y, x % y)


if __name__ == '__main__':
    x, y = map(int, input().split())
    print('math.gcd:', math.gcd(x, y))
    print('iteration method:', iter_gcd(x, y))
    print('euclid method:', euclid_gcd(x, y))
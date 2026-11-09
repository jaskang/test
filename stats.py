"""Small statistics helpers."""


def mean(xs):
    return sum(xs) / len(xs)


def median(xs):
    s = sorted(xs)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]

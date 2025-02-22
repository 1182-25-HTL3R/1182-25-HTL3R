def M(n: int) -> int:
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10
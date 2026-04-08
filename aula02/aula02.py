def fatorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)
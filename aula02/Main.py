import tracemalloc


# def fatorial_iterativo(n):
#    r = 1
#    for i in range(1, n + 1):
#        r *= i
#    return r

def fatorial_recursivo(n):
    if n < 2:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)


tracemalloc.start()

# fatorial_iterativo(10)
fatorial_recursivo(100)

snapshot = tracemalloc.take_snapshot()

print(snapshot)

top_stats = snapshot.statistics('lineno')
for stat in top_stats[:5]:
    print(stat)

tracemalloc.stop()
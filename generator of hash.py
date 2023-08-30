def generator(N):
    for _ in range(N):
        yield "#" * N

N = 3
typer = generator(N)

for row in typer:
    print(row)

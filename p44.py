def multiplication(n):
    prod=""
    for i in range(1,11):
        prod+=f"{n}x{i}={n*i}\n"
    with open(f"Table/prod{n}","w") as f:
        f.write(prod)
for i in range(2,21):
    multiplication(i)
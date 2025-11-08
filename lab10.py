n = int(input().strip())
first = True

for d in range(1, n + 1):
    if n % d == 0:
        if not first:
            print(' ', end='')
        print(d, end='')
        first = False

print()


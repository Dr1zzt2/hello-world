i = 0
j = 1
k = 0
x = 1
fib = 0
while i < 1 or i > 30:
    msg = "Write a number.(Max:30)"
    print(msg)
    try:
        i = int(input())
    except ValueError:
        continue
for i in range(0,i):
    print(f"{x}.".ljust(10 - len(str(fib))),f"{fib}")
    fib = j + k
    j = k
    k = fib
    x = x + 1
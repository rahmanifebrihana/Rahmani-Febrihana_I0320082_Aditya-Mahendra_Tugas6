print("====== Program Pengulangan Bilangan Prima ======")
a = 10
b = 25

for x in range(a,b):
    if x > 1:
        for y in range(2,x):
            if (x % y) == 0:
                print(x, "bukan bilangan prima")
                break
        else:
            print(x, "adalah bilangan prima")

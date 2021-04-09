print("====== Program Menghitung Nilai Rata-Rata ======")

#menginput banyaknya data
n = int(input("Banyaknya data yang ada yaitu: "))
data=[]
total = 0

for x in range(0, n):
    y = int(input("Masukkan angka ke-%d: " % (x + 1)))
    data.append(y)
    total += data[x]
    rata_rata = total / n
print("Hasil rata-rata dari data keseluruhan yaitu: %0.1f" % rata_rata)

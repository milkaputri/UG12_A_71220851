n = str(input("Masukan nama : "))
akhir = 0

for i in range(len(n)):
    akhir +=1
    print(n[:akhir])
for i in range(len(n)):
    akhir -= 1
    print(n[:akhir])
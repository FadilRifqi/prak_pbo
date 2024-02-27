batas_bawah = int(input("batas bawah : "))
batas_atas = int(input("batas atas : "))
total = int(0)

if batas_atas <= 0 or batas_bawah <= 0:
    print("Batas bawah dan batas atas yang dimasukkan tidak boleh di bawah Nol")
else:
    for i in range(batas_bawah,batas_atas):
        if i % 2 != 0:
            print(i)
            total += i
    print("total : " , total)



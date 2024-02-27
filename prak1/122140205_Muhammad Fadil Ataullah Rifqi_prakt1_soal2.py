jari_jari = int(input("jari jari : "))

if jari_jari <= 0:
    print("jari-jari lingkaran tidak boleh negatif")
else:
    keliling = 2 * 3.14 * jari_jari
    luas = 3.14 * jari_jari**2
    print("Luas : ", luas)
    print("keliling : ", keliling)

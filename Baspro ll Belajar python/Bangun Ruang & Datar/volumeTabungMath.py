import math

jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))

tinggi_tabung = float(input("Masukkan tinggi tabung: "))
volume_tabung = math.pi * jari_jari_tabung * jari_jari_tabung * tinggi_tabung

print("Volume tabung dengan jari-jari", jari_jari_tabung, "dan tinggi", tinggi_tabung, "adalah", volume_tabung)

#ini adalah versi yang menggunakan impor math
#untuk versi manual, buka "volumeTabung"
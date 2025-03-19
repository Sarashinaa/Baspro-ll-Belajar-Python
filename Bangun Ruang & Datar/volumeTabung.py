pi = (22/7)

jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))

tinggi_tabung = float(input("Masukkan tinggi tabung: "))
volume_tabung = pi * jari_jari_tabung * jari_jari_tabung * tinggi_tabung

print("Volume tabung dengan jari-jari", jari_jari_tabung, "dan tinggi", tinggi_tabung, "adalah", volume_tabung)

#catatan:
#di code ini, nilai pi saya definisikan manual tanpa meng-import math. hasil mungkin akan sedikit berbeda
#"volumeTabungMath" adalah versi yang menggunakan import math
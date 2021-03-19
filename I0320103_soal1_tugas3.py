#TOGAR OBAJA NAINGGOLAN
#NIM I0320103
#KELAS C
#Tugas 3 Soal 1

print('Daftar 10 anggota tim cerdas cermat TI 20')
list = ['Alvin','Attar','Bagus','Cita','Hasan','Fadhila','Halidya','Raysa','Vicentia','Zafira']
print('Siapakah oraang yang berada pada indeks ke 4 ? :', list[4])
print('Siapakah oraang yang berada pada indeks ke 6 dan 7 ? :', list[6:8])
#Pergantian orang terjadi karena adanya urusan mendesak
list[3] = 'Rizal'
list[5] = 'Efa'
list[9] = 'Salsabila'
#Penambahan orang sebagai cadangan pada hari-H
Tim = list + ['Alfina', 'Nurwicaksana']
#Mengoreksi kembali data tim sebanyak 3 kali
cek = Tim * 3
print(cek)
print('Daftar final anggota tim cerdas cermat TI 20 :', Tim)
print('Selamat dan semoga sukses!')
